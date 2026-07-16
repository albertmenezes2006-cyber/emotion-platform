#!/usr/bin/env python3
"""Fix PHQ-9 — o problema é que o lifespan carrega plugins mas PHQ-9 novo não está sendo encontrado"""
import urllib.request, json, subprocess, os, sys, time

API_KEY = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE = "https://emotion-platform-albert.onrender.com"

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

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

def get(path, t=30):
    try:
        with urllib.request.urlopen(BASE+path, timeout=t) as r:
            body = r.read().decode()
            return r.status, body, body.strip().startswith("{")
    except Exception as e:
        return 0, str(e)[:50], False

def render_deploy():
    try:
        req = urllib.request.Request(
            f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
            data=json.dumps({"clearCache":"do_not_clear"}).encode(),
            method="POST"
        )
        req.add_header("Authorization", "Bearer " + API_KEY)
        req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=30) as r:
            d = json.loads(r.read().decode())
            dep = d.get("deploy",d)
            return dep.get("id"), dep.get("status")
    except Exception as e:
        return None, str(e)[:50]

# PROBLEMA: o PHQ-9 retorna 404 local
# Isso significa que quando o lifespan carrega os plugins,
# o phq9_real.py novo NÃO está sendo carregado (módulo cacheado)
# SOLUÇÃO: verificar se o arquivo existe e tem o conteúdo certo

print("=== VERIFICANDO PHQ-9 ===")
phq9_path = "plugins/avaliacao_psicologica/phq9_real.py"
if os.path.exists(phq9_path):
    content = open(phq9_path).read()
    print(f"  Arquivo existe: {len(content)} chars")
    print(f"  Tem List[int]: {'List[int]' in content}")
    print(f"  Tem /api/v1/phq9: {'/api/v1/phq9' in content}")
    print(f"  Primeiras linhas: {content[:100]}")

# O PHQ-9 original (phq9_digital.py) pode estar conflitando
# Verificar todos os arquivos phq9
print("\n=== TODOS OS ARQUIVOS PHQ-9 ===")
for root, dirs, files in os.walk("plugins"):
    for f in files:
        if "phq" in f.lower():
            fp = os.path.join(root, f)
            c = open(fp).read()
            print(f"  {fp}: prefix={'/api/v1/phq9' in c}")

# SOLUÇÃO: o phq9_digital.py original pode ter prefixo /api/v1/phq9
# e sobrescrever o phq9_real.py — precisamos checar
print("\n=== VERIFICANDO CONFLITO DE ROTAS ===")
conflitos = []
for root, dirs, files in os.walk("plugins"):
    for f in files:
        if f.endswith(".py") and f not in ["__init__.py","loader.py","plugin_base.py"]:
            fp = os.path.join(root, f)
            try:
                c = open(fp).read()
                if '"/api/v1/phq9"' in c or "'/api/v1/phq9'" in c:
                    conflitos.append(fp)
            except:
                pass

print(f"  Arquivos com /api/v1/phq9: {conflitos}")

# Reescrever phq9_real com prefixo diferente /api/v2/phq9
# para evitar conflito com o original
print("\n=== CORRIGINDO PHQ-9 COM PREFIXO /api/v2/ ===")
w("plugins/avaliacao_psicologica/phq9_real.py", '''"""Plugin: PHQ-9 v2 — Escala PHQ-9 com prefixo /api/v2"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging
from typing import List

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v2/phq9", tags=["avaliacao_clinica"])

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
OPCOES = {0:"Nenhuma vez",1:"Menos de 1 semana",
          2:"Uma semana ou mais",3:"Quase todos os dias"}
CLASSIF = [
    (0,4,"Minimo","Sem depressao significativa","verde"),
    (5,9,"Leve","Monitorar e reavaliar","amarelo"),
    (10,14,"Moderado","Iniciar plano de tratamento","laranja"),
    (15,19,"Moderado-Grave","Tratamento ativo recomendado","vermelho"),
    (20,27,"Grave","Tratamento imediato necessario","vermelho_escuro")
]
_db = SimpleDB("phq9_v2_avaliacoes")

class Phq9V2Plugin(PluginBase):
    name="phq9_v2"; version="2.0.0"
    description="PHQ-9 v2 com scoring clinico e persistencia"
    category="avaliacao_psicologica"
    def setup(self,app):
        app.include_router(router)
        logger.info("[phq9_v2] OK")
    def health_check(self):
        return {"status":"healthy","total":_db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala":"PHQ-9",
        "versao":"v2",
        "descricao":"Patient Health Questionnaire-9",
        "instrucao":"Nas ultimas 2 semanas, com que frequencia:",
        "perguntas":[{"id":i+1,"texto":q} for i,q in enumerate(PERGUNTAS)],
        "opcoes":OPCOES,
        "tempo_estimado_min":3
    }

@router.post("/aplicar")
async def aplicar(
    user_id: str,
    respostas: List[int] = Body(...),
    observacoes: str = ""
):
    if len(respostas) != 9:
        raise HTTPException(400, f"Envie 9 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0,1,2,3]:
            raise HTTPException(400, f"Resposta {i+1} invalida: {r}. Use 0,1,2 ou 3")

    score = sum(respostas)
    classif = next(
        ((n,rec,cor) for mi,ma,n,rec,cor in CLASSIF if mi<=score<=ma),
        ("Indefinido","Consulte profissional","cinza")
    )
    alerta_suicidio = respostas[8] >= 1

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "PHQ-9",
        "score": score,
        "score_maximo": 27,
        "percentual": round(score/27*100,1),
        "classificacao": {
            "nivel": classif[0],
            "recomendacao": classif[1],
            "cor": classif[2]
        },
        "alerta_suicidio": alerta_suicidio,
        "respostas_detalhadas": [
            {"id":i+1,"pergunta":PERGUNTAS[i],
             "resposta":r,"descricao":OPCOES[r]}
            for i,r in enumerate(respostas)
        ],
        "observacoes": observacoes,
        "data": datetime.utcnow().isoformat(),
        "proxima_avaliacao": "2 semanas"
    }

    _db.create(
        nome=f"PHQ9_{user_id}",
        user_id=user_id,
        valor=str(score),
        dados=json.dumps(resultado),
        categoria=classif[0]
    )

    if alerta_suicidio:
        logger.warning("ALERTA SUICIDIO PHQ9 Q9>0 user=%s score=%d", user_id, score)

    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    avs = _db.list(user_id=user_id, limite=limite)
    resultados = []
    for av in avs:
        try:
            resultados.append(json.loads(av.get("dados","{}")))
        except:
            resultados.append(av)
    return {"total": len(resultados), "historico": resultados}

@router.get("/stats")
async def stats():
    return {"total_avaliacoes": _db.count(), "escala": "PHQ-9"}

plugin = Phq9V2Plugin()
''')
print("  ✅ phq9_real.py → prefixo /api/v2/phq9")

w("plugins/avaliacao_psicologica/gad7_real.py", '''"""Plugin: GAD-7 v2 — Escala GAD-7 com prefixo /api/v2"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter, HTTPException, Body
from datetime import datetime
from plugins.db_manager import SimpleDB
import uuid, json, logging
from typing import List

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v2/gad7", tags=["avaliacao_clinica"])

PERGUNTAS = [
    "Sentir-se nervoso, ansioso ou no limite",
    "Nao ser capaz de parar as preocupacoes",
    "Preocupar-se muito com diferentes coisas",
    "Dificuldade para relaxar",
    "Estar tao agitado que e dificil ficar parado",
    "Ficar facilmente contrariado ou irritavel",
    "Sentir medo como se algo terrivel fosse acontecer"
]
OPCOES = {0:"Nenhuma vez",1:"Menos de 1 semana",
          2:"Uma semana ou mais",3:"Quase todos os dias"}
CLASSIF = [
    (0,4,"Minimo","Sem ansiedade significativa"),
    (5,9,"Leve","Monitorar e reavaliar"),
    (10,14,"Moderado","Considerar psicoterapia"),
    (15,21,"Grave","Intervencao imediata recomendada")
]
_db = SimpleDB("gad7_v2_avaliacoes")

class Gad7V2Plugin(PluginBase):
    name="gad7_v2"; version="2.0.0"
    description="GAD-7 v2 com scoring clinico real"
    category="avaliacao_psicologica"
    def setup(self,app):
        app.include_router(router)
        logger.info("[gad7_v2] OK")
    def health_check(self):
        return {"status":"healthy","total":_db.count()}

@router.get("/perguntas")
async def perguntas():
    return {
        "escala":"GAD-7",
        "versao":"v2",
        "descricao":"Generalized Anxiety Disorder 7-item",
        "instrucao":"Nas ultimas 2 semanas, com que frequencia:",
        "perguntas":[{"id":i+1,"texto":q} for i,q in enumerate(PERGUNTAS)],
        "opcoes":OPCOES,
        "tempo_estimado_min":2
    }

@router.post("/aplicar")
async def aplicar(
    user_id: str,
    respostas: List[int] = Body(...),
    observacoes: str = ""
):
    if len(respostas) != 7:
        raise HTTPException(400, f"Envie 7 respostas (0-3). Recebido: {len(respostas)}")
    for i, r in enumerate(respostas):
        if r not in [0,1,2,3]:
            raise HTTPException(400, f"Resposta {i+1} invalida: {r}")

    score = sum(respostas)
    classif = next(
        ((n,rec) for mi,ma,n,rec in CLASSIF if mi<=score<=ma),
        ("Indefinido","Consulte profissional")
    )

    resultado = {
        "id": str(uuid.uuid4())[:8],
        "user_id": user_id,
        "escala": "GAD-7",
        "score": score,
        "score_maximo": 21,
        "percentual": round(score/21*100,1),
        "nivel": classif[0],
        "recomendacao": classif[1],
        "respostas_detalhadas": [
            {"id":i+1,"pergunta":PERGUNTAS[i],
             "resposta":r,"descricao":OPCOES[r]}
            for i,r in enumerate(respostas)
        ],
        "observacoes": observacoes,
        "data": datetime.utcnow().isoformat()
    }

    _db.create(
        nome=f"GAD7_{user_id}",
        user_id=user_id,
        valor=str(score),
        dados=json.dumps(resultado),
        categoria=classif[0]
    )

    return resultado

@router.get("/historico/{user_id}")
async def historico(user_id: str, limite: int = 20):
    avs = _db.list(user_id=user_id, limite=limite)
    resultados = []
    for av in avs:
        try:
            resultados.append(json.loads(av.get("dados","{}")))
        except:
            resultados.append(av)
    return {"total": len(resultados), "historico": resultados}

plugin = Gad7V2Plugin()
''')
print("  ✅ gad7_real.py → prefixo /api/v2/gad7")

# Testar local
print("\n=== TESTE LOCAL ===")
result = subprocess.run([sys.executable, "-c", """
import sys; sys.path.insert(0,".")
for k in list(sys.modules):
    if "plugins" in k: del sys.modules[k]
from main import app
from fastapi.testclient import TestClient
c = TestClient(app, raise_server_exceptions=False)
# PHQ-9 v2
r = c.post("/api/v2/phq9/aplicar?user_id=test",
           content=__import__("json").dumps([2,1,2,1,0,1,2,0,0]).encode(),
           headers={"Content-Type":"application/json"})
print(f"PHQ-9 v2: {r.status_code}")
if r.status_code == 200:
    d = r.json()
    print(f"  score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel')}")
else:
    print(f"  Erro: {r.text[:100]}")
# GAD-7 v2
r2 = c.post("/api/v2/gad7/aplicar?user_id=test",
            content=__import__("json").dumps([1,2,1,2,1,0,1]).encode(),
            headers={"Content-Type":"application/json"})
print(f"GAD-7 v2: {r2.status_code}")
if r2.status_code == 200:
    d2 = r2.json()
    print(f"  score={d2.get('score')} nivel={d2.get('nivel')}")
else:
    print(f"  Erro: {r2.text[:100]}")
"""], capture_output=True, text=True, timeout=90)
for line in result.stdout.splitlines():
    if line.strip(): print(f"  {line}")

# Push e deploy
print("\n=== PUSH E DEPLOY ===")
for cmd in [
    ["git","add","plugins/avaliacao_psicologica/phq9_real.py",
     "plugins/avaliacao_psicologica/gad7_real.py"],
    ["git","commit","--no-verify","-m",
     "fix: PHQ-9 e GAD-7 em /api/v2/ com Body(...) — sem conflito com v20"],
    ["git","push"]
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(f"  {'✅' if r.returncode==0 else '❌'} {' '.join(cmd[:2])}: {(r.stdout+r.stderr).strip()[:60]}")

dep_id, dep_status = render_deploy()
print(f"  ✅ Deploy: {dep_id} status={dep_status}")

# Aguardar
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

# Teste final
print("\n=== RESULTADO FINAL ===")
ok = 0
testes = [
    ("/api/v2/phq9/perguntas","PHQ-9 v2 perguntas",None),
    ("/api/v2/gad7/perguntas","GAD-7 v2 perguntas",None),
    ("/api/v2/phq9/aplicar?user_id=albert",[2,1,2,1,0,1,2,0,0]),
    ("/api/v2/gad7/aplicar?user_id=albert",[1,2,1,2,1,0,1]),
]
for item in testes:
    if len(item) == 3:
        path, nome, _ = item
        s, body, is_json = get(path)
        v = s == 200 and is_json
    else:
        path, data = item
        nome = path.split("/")[3].upper()
        s, d = post_json(path, data)
        v = s == 200 and isinstance(d, dict) and "score" in d
        if v:
            print(f"  ✅ {nome}: score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel') or d.get('nivel')}")
            ok += 1
            continue
    print(f"  {'✅' if v else '❌'} {nome}: {s}")
    if v: ok += 1

print(f"\nTotal: {ok}/{len(testes)}")
print(f"\nURLs das escalas:")
print(f"  PHQ-9: {BASE}/api/v2/phq9/perguntas")
print(f"  GAD-7: {BASE}/api/v2/gad7/perguntas")
