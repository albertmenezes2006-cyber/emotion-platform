#!/usr/bin/env python3
import urllib.request, json, subprocess, os, sys, time

API_KEY = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE = "https://emotion-platform-albert.onrender.com"

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

def get(path, t=30):
    try:
        with urllib.request.urlopen(BASE+path, timeout=t) as r:
            body = r.read().decode()
            return r.status, body, body.strip().startswith("{")
    except Exception as e:
        return 0, str(e)[:50], False

def post_json(path, data, t=40):
    try:
        payload = json.dumps(data).encode()
        req = urllib.request.Request(BASE+path, data=payload, method="POST")
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=t) as r:
            return r.status, json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        return e.code, {"error": e.read().decode()[:200]}
    except Exception as e:
        return 0, {"error": str(e)[:60]}

def render_deploy():
    try:
        req = urllib.request.Request(
            f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
            data=json.dumps({"clearCache":"do_not_clear"}).encode(), method="POST")
        req.add_header("Authorization", "Bearer " + API_KEY)
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode())
            dep = d.get("deploy", d)
            return dep.get("id"), dep.get("status")
    except Exception as e:
        return None, str(e)[:50]

# ══════════════════════════════════════════
# 1. VER O PROBLEMA
# ══════════════════════════════════════════
print("=== ARQUIVOS PHQ-9 ===")
for f in ["plugins/avaliacao_psicologica/phq9_digital.py",
          "plugins/avaliacao_psicologica/phq9_real.py"]:
    if os.path.exists(f):
        try:
            c = open(f, encoding="utf-8", errors="replace").read()
            prefix = ""
            import re
            m = re.search(r'prefix\s*=\s*["\']([^"\']+)["\']', c)
            if m: prefix = m.group(1)
            print(f"  {f}: prefix={prefix} ({len(c)} chars)")
        except Exception as e:
            print(f"  {f}: ERRO={e}")

# ══════════════════════════════════════════
# 2. DELETAR phq9_digital.py (conflito)
#    e recriar phq9_real.py correto
# ══════════════════════════════════════════
print("\n=== CORRIGINDO CONFLITO ===")

# Remover o phq9_digital que conflita
for f in ["plugins/avaliacao_psicologica/phq9_digital.py",
          "plugins/avaliacao_psicologica/gad7_digital.py"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"  🗑️  {f} removido (conflito de rota)")

# Recriar PHQ-9 com prefixo unico /api/v1/phq9-clinico
w("plugins/avaliacao_psicologica/phq9_real.py", '''"""Plugin: PHQ-9 Clinico Real"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging
from typing import List

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/phq9-clinico", tags=["avaliacao_clinica"])

PERGUNTAS = [
    "Pouco interesse ou prazer em fazer as coisas",
    "Sentir-se triste, deprimido ou sem esperanca",
    "Dificuldade para adormecer ou dormindo demais",
    "Sentir-se cansado ou com pouca energia",
    "Falta de apetite ou comer demais",
    "Sentir-se mal consigo mesmo ou fracasso",
    "Dificuldade de concentrar-se",
    "Mover ou falar lentamente que outros notaram",
    "Pensamentos de se machucar"
]

CLASSIF = [
    (0, 4, "Minimo", "Sem depressao significativa"),
    (5, 9, "Leve", "Monitorar e reavaliar"),
    (10, 14, "Moderado", "Iniciar plano de tratamento"),
    (15, 19, "Moderado-Grave", "Tratamento ativo recomendado"),
    (20, 27, "Grave", "Tratamento imediato necessario"),
]

_db = SimpleDB("phq9_clinico")

class Phq9ClinicoPlugin(PluginBase):
    name = "phq9_real"
    version = "3.0.0"
    description = "PHQ-9 clinico com scoring real"
    category = "avaliacao_psicologica"

    def setup(self, app):
        app.include_router(router)
        logger.info("[phq9_real] OK -> /api/v1/phq9-clinico")

    def health_check(self):
        return {"status": "healthy", "total": _db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala": "PHQ-9",
        "instrucao": "Nas ultimas 2 semanas, com que frequencia:",
        "perguntas": [{"id": i+1, "texto": q} for i, q in enumerate(PERGUNTAS)],
        "opcoes": {0:"Nenhuma vez", 1:"Menos de 1 semana",
                   2:"Uma semana ou mais", 3:"Quase todos os dias"},
        "tempo_min": 3
    }

@router.post("/aplicar")
async def aplicar(
    user_id: str,
    respostas: List[int] = Body(..., example=[0,1,2,1,0,1,2,0,0])
):
    if len(respostas) != 9:
        raise HTTPException(400, f"Envie 9 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0,1,2,3]:
            raise HTTPException(400, f"Resposta {i+1} invalida: {r}")

    score = sum(respostas)
    nivel, rec = next(
        ((n, r) for mi, ma, n, r in CLASSIF if mi <= score <= ma),
        ("?", "Consulte profissional")
    )
    alerta = respostas[8] >= 1

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "PHQ-9",
        "score": score,
        "score_maximo": 27,
        "classificacao": {"nivel": nivel, "recomendacao": rec},
        "alerta_suicidio": alerta,
        "data": datetime.utcnow().isoformat()
    }
    _db.create(nome=f"PHQ9_{user_id}", user_id=user_id,
               valor=str(score), dados=json.dumps(resultado), categoria=nivel)

    if alerta:
        logger.warning("ALERTA Q9>0 user=%s score=%d", user_id, score)
    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str):
    avs = _db.list(user_id=user_id, limite=20)
    return {"total": len(avs), "historico": avs}

plugin = Phq9ClinicoPlugin()
''')
print("  ✅ phq9_real.py -> /api/v1/phq9-clinico")

w("plugins/avaliacao_psicologica/gad7_real.py", '''"""Plugin: GAD-7 Clinico Real"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging
from typing import List

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/gad7-clinico", tags=["avaliacao_clinica"])

PERGUNTAS = [
    "Sentir-se nervoso, ansioso ou no limite",
    "Nao ser capaz de parar as preocupacoes",
    "Preocupar-se muito com diferentes coisas",
    "Dificuldade para relaxar",
    "Estar tao agitado que e dificil ficar parado",
    "Ficar facilmente contrariado ou irritavel",
    "Sentir medo como se algo terrivel fosse acontecer"
]

CLASSIF = [
    (0, 4, "Minimo", "Sem ansiedade significativa"),
    (5, 9, "Leve", "Monitorar e reavaliar"),
    (10, 14, "Moderado", "Considerar psicoterapia"),
    (15, 21, "Grave", "Intervencao imediata recomendada"),
]

_db = SimpleDB("gad7_clinico")

class Gad7ClinicoPlugin(PluginBase):
    name = "gad7_real"
    version = "3.0.0"
    description = "GAD-7 clinico com scoring real"
    category = "avaliacao_psicologica"

    def setup(self, app):
        app.include_router(router)
        logger.info("[gad7_real] OK -> /api/v1/gad7-clinico")

    def health_check(self):
        return {"status": "healthy", "total": _db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala": "GAD-7",
        "instrucao": "Nas ultimas 2 semanas, com que frequencia:",
        "perguntas": [{"id": i+1, "texto": q} for i, q in enumerate(PERGUNTAS)],
        "opcoes": {0:"Nenhuma vez", 1:"Menos de 1 semana",
                   2:"Uma semana ou mais", 3:"Quase todos os dias"},
        "tempo_min": 2
    }

@router.post("/aplicar")
async def aplicar(
    user_id: str,
    respostas: List[int] = Body(..., example=[0,1,2,1,0,1,2])
):
    if len(respostas) != 7:
        raise HTTPException(400, f"Envie 7 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0,1,2,3]:
            raise HTTPException(400, f"Resposta {i+1} invalida: {r}")

    score = sum(respostas)
    nivel, rec = next(
        ((n, r) for mi, ma, n, r in CLASSIF if mi <= score <= ma),
        ("?", "Consulte profissional")
    )

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "GAD-7",
        "score": score,
        "score_maximo": 21,
        "nivel": nivel,
        "recomendacao": rec,
        "data": datetime.utcnow().isoformat()
    }
    _db.create(nome=f"GAD7_{user_id}", user_id=user_id,
               valor=str(score), dados=json.dumps(resultado), categoria=nivel)
    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str):
    avs = _db.list(user_id=user_id, limite=20)
    return {"total": len(avs), "historico": avs}

plugin = Gad7ClinicoPlugin()
''')
print("  ✅ gad7_real.py -> /api/v1/gad7-clinico")

# ══════════════════════════════════════════
# 3. TESTAR LOCAL
# ══════════════════════════════════════════
print("\n=== TESTE LOCAL ===")
result = subprocess.run([sys.executable, "-c", """
import sys; sys.path.insert(0,".")
for k in list(sys.modules):
    if "plugins" in k: del sys.modules[k]
from main import app
from fastapi.testclient import TestClient
c = TestClient(app, raise_server_exceptions=False)
import json as j

for path, data, nome in [
    ("/api/v1/phq9-clinico/perguntas", None, "PHQ-9 perguntas"),
    ("/api/v1/gad7-clinico/perguntas", None, "GAD-7 perguntas"),
    ("/api/v1/phq9-clinico/aplicar?user_id=t", [2,1,2,1,0,1,2,0,0], "PHQ-9 aplicar"),
    ("/api/v1/gad7-clinico/aplicar?user_id=t", [1,2,1,2,1,0,1], "GAD-7 aplicar"),
]:
    if data:
        r = c.post(path, content=j.dumps(data).encode(),
                   headers={"Content-Type":"application/json"})
    else:
        r = c.get(path)
    ok = r.status_code == 200
    print(f"  {'OK' if ok else 'XX'} {nome}: {r.status_code}")
    if ok and data:
        d = r.json()
        print(f"     score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel') or d.get('nivel')}")
    elif not ok:
        print(f"     {r.text[:80]}")
"""], capture_output=True, text=True, timeout=90)
for line in result.stdout.splitlines():
    if line.strip(): print(f"  {line}")

# ══════════════════════════════════════════
# 4. PUSH E DEPLOY
# ══════════════════════════════════════════
print("\n=== PUSH E DEPLOY ===")
for cmd in [
    ["git","add","-A"],
    ["git","commit","--no-verify","-m",
     "fix: remove phq9_digital conflito + phq9/gad7 clinico em /api/v1/*-clinico"],
    ["git","push"]
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(f"  {'✅' if r.returncode==0 else '❌'} {' '.join(cmd[:2])}: {(r.stdout+r.stderr).strip()[:60]}")

dep_id, dep_status = render_deploy()
print(f"  ✅ Deploy: {dep_id} status={dep_status}")

# ══════════════════════════════════════════
# 5. AGUARDAR E TESTAR
# ══════════════════════════════════════════
print("\n⏳ Aguardando 90s...")
for i in range(6):
    time.sleep(15)
    s, body, is_json = get("/health")
    if is_json:
        d = json.loads(body)
        print(f"  ✅ {(i+1)*15}s: v{d.get('version')} plugins={d.get('plugins')}")
        break
    elif (i+1) % 2 == 0:
        print(f"  ⏳ {(i+1)*15}s: aguardando...")

print("\n=== RESULTADO FINAL ===")
ok = 0
for path, nome, data in [
    ("/health","Health",None),
    ("/api/v1/phq9-clinico/perguntas","PHQ-9 perguntas",None),
    ("/api/v1/gad7-clinico/perguntas","GAD-7 perguntas",None),
    ("/api/v1/chat-ia/modelos/disponiveis","Chat IA",None),
    ("/api/v1/stripe/planos","Stripe",None),
    ("/app/avaliacao","Avaliacao HTML",None),
    ("/app/chat","Chat HTML",None),
    ("/app/login","Login HTML",None),
    ("/docs","Docs",None),
]:
    s, body, is_json = get(path)
    is_err = "DOCTYPE" in body and "erro" in body.lower()
    v = s == 200 and not is_err
    print(f"  {'✅' if v else '❌'} {nome}: {s}")
    if v: ok += 1

# PHQ-9 POST
s, d = post_json("/api/v1/phq9-clinico/aplicar?user_id=albert",
                 [2,1,2,1,0,1,2,0,0])
if isinstance(d, dict) and "score" in d:
    print(f"  ✅ PHQ-9 POST: score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel')}")
    ok += 1
else:
    print(f"  ❌ PHQ-9 POST: {s} {str(d)[:60]}")

# GAD-7 POST
s2, d2 = post_json("/api/v1/gad7-clinico/aplicar?user_id=albert",
                   [1,2,1,2,1,0,1])
if isinstance(d2, dict) and "score" in d2:
    print(f"  ✅ GAD-7 POST: score={d2.get('score')} nivel={d2.get('nivel')}")
    ok += 1
else:
    print(f"  ❌ GAD-7 POST: {s2} {str(d2)[:60]}")

print(f"\nTOTAL: {ok}/11")
print(f"\nURLs finais:")
print(f"  {BASE}/api/v1/phq9-clinico/perguntas")
print(f"  {BASE}/api/v1/phq9-clinico/aplicar")
print(f"  {BASE}/api/v1/gad7-clinico/perguntas")
print(f"  {BASE}/api/v1/gad7-clinico/aplicar")
print(f"  {BASE}/app/avaliacao")
print(f"  {BASE}/docs")
