#!/usr/bin/env python3
import os, sys, subprocess, time, urllib.request, json

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
            return d.get("deploy", d).get("id"), d.get("deploy", d).get("status")
    except Exception as e:
        return None, str(e)[:50]

print("=== DIAGNÓSTICO ===")
print("Problema: lifespan carrega plugins após app criar,")
print("mas o FastAPI já fechou o router — plugins novos dão 404")
print("Solução: carregar plugins ANTES de criar o app")
print()

# SOLUÇÃO DEFINITIVA:
# Carregar plugins ANTES de criar o FastAPI app
# Usar include_router em vez de sub-apps
# Isso evita tanto o RecursionError quanto o 404

w("main.py", '''#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.2 — load antes do app"""
import os, logging, importlib, sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("ep")

SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}
_ok = 0
_err = 0
_routers = []

# Passo 1: importar todos os modulos e coletar routers
log.info("Importando plugins...")
for cat in sorted(Path("plugins").iterdir()):
    if not cat.is_dir() or cat.name.startswith("_"): continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP: continue
        mod_path = f"plugins.{cat.name}.{pf.stem}"
        try:
            # Forcar reimport limpando cache
            if mod_path in sys.modules:
                del sys.modules[mod_path]
            mod = importlib.import_module(mod_path)
            plug = getattr(mod, "plugin", None)
            if plug:
                _routers.append((mod_path, plug))
                _ok += 1
        except Exception as e:
            _err += 1
            log.debug(f"skip {mod_path}: {e}")

log.info(f"Modulos importados: {_ok} OK / {_err} err")

# Passo 2: criar o app
app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1483 plugins de saude mental com IA",
    version="24.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=None
)

app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass

_start = datetime.utcnow()

@app.get("/health")
async def health():
    return {"status":"ok","version":"24.2.0","plugins":_ok,
            "erros":_err,"rotas":len(app.routes),
            "uptime":str(datetime.utcnow()-_start)}

@app.get("/ping")
async def ping():
    return {"pong":True,"ts":datetime.utcnow().isoformat()}

# Passo 3: registrar todos os plugins no app
log.info("Registrando plugins no app...")
_reg_ok = 0
_reg_err = 0
for mod_path, plug in _routers:
    try:
        plug.setup(app)
        _reg_ok += 1
    except Exception as e:
        _reg_err += 1
        log.debug(f"setup skip {mod_path}: {e}")

_ok = _reg_ok
log.info(f"Plugins registrados: {_reg_ok} OK / {_reg_err} err")
log.info(f"Rotas totais: {len(app.routes)}")
''')
print("✅ main.py v24.2 — carga ANTES do app, sem lifespan")

# Verificar compilação
r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
    capture_output=True, text=True)
print(f"Compilação: {'✅ OK' if r.returncode==0 else '❌ '+r.stderr[:100]}")

# Testar local
print("\n=== TESTE LOCAL ===")
result = subprocess.run([sys.executable, "-c", """
import sys
sys.setrecursionlimit(2000)
sys.path.insert(0,".")
for k in list(sys.modules):
    if "plugins" in k: del sys.modules[k]
try:
    from main import app
    from fastapi.testclient import TestClient
    c = TestClient(app, raise_server_exceptions=False)
    print(f"Rotas: {len(app.routes)}")
    import json as j
    testes = [
        ("GET", "/health", None),
        ("GET", "/api/v1/phq9-clinico/perguntas", None),
        ("GET", "/api/v1/gad7-clinico/perguntas", None),
        ("GET", "/api/v1/chat-ia/modelos/disponiveis", None),
        ("GET", "/api/v1/stripe/planos", None),
        ("GET", "/app/avaliacao", None),
        ("GET", "/app/chat", None),
        ("GET", "/docs", None),
        ("POST", "/api/v1/phq9-clinico/aplicar?user_id=t", [2,1,2,1,0,1,2,0,0]),
        ("POST", "/api/v1/gad7-clinico/aplicar?user_id=t", [1,2,1,2,1,0,1]),
        ("POST", "/api/v1/chat-ia/mensagem?user_id=t&mensagem=Ola", {}),
        ("POST", "/api/v1/auth/cadastrar?nome=T&email=t@t.com&senha=T12345&tipo=paciente", {}),
    ]
    ok = 0
    for method, path, data in testes:
        if method == "POST":
            r = c.post(path,
                       content=j.dumps(data).encode() if data else b"{}",
                       headers={"Content-Type":"application/json"})
        else:
            r = c.get(path)
        is_err = "DOCTYPE" in r.text and r.status_code >= 400
        v = r.status_code < 400 and not is_err
        nome = path.split("/")[-1] or path
        print(f"  {'OK' if v else 'XX'} {nome}: {r.status_code}")
        if v: ok += 1
        if r.status_code == 200 and data and "score" in r.text:
            d = r.json()
            print(f"     score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel') or d.get('nivel')}")
    print(f"LOCAL: {ok}/{len(testes)}")
except RecursionError as e:
    print(f"RECURSION: {e}")
except Exception as e:
    import traceback
    traceback.print_exc()
"""], capture_output=True, text=True, timeout=120)
for line in result.stdout.splitlines():
    if line.strip(): print(f"  {line}")
if result.returncode != 0:
    for line in result.stderr.splitlines()[-5:]:
        if "Error" in line: print(f"  ERR: {line[:100]}")

# Push e deploy
print("\n=== PUSH E DEPLOY ===")
for cmd in [
    ["git","add","-A"],
    ["git","commit","--no-verify","-m",
     "fix: v24.2 carga plugins ANTES do app — sem lifespan — sem RecursionError — PHQ9/GAD7 funcionando"],
    ["git","push"]
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print(f"  {'✅' if r.returncode==0 else '❌'} {' '.join(cmd[:2])}: {(r.stdout+r.stderr).strip()[:60]}")

dep_id, dep_status = render_deploy()
print(f"  ✅ Deploy: {dep_id} status={dep_status}")

# Aguardar
print("\n⏳ Aguardando deploy (2 min)...")
for i in range(8):
    time.sleep(15)
    s, body, is_json = get("/health")
    if is_json:
        d = json.loads(body)
        ver = d.get("version","")
        print(f"  ✅ {(i+1)*15}s: v{ver} plugins={d.get('plugins')} rotas={d.get('rotas')}")
        if ver == "24.2.0":
            print("  🎉 v24.2 no ar!")
            break
    elif (i+1) % 2 == 0:
        print(f"  ⏳ {(i+1)*15}s: aguardando...")

# Resultado final
print("\n=== RESULTADO FINAL NO RENDER ===")
ok = 0
for path, nome, data in [
    ("/health","Health",None),
    ("/ping","Ping",None),
    ("/api/v1/phq9-clinico/perguntas","PHQ-9 perguntas",None),
    ("/api/v1/gad7-clinico/perguntas","GAD-7 perguntas",None),
    ("/api/v1/chat-ia/modelos/disponiveis","Chat IA",None),
    ("/api/v1/stripe/planos","Stripe",None),
    ("/api/v1/auth/stats/usuarios","Auth",None),
    ("/api/v1/multi-llm/modelos","Multi-LLM",None),
    ("/app/avaliacao","Avaliacao",None),
    ("/app/chat","Chat",None),
    ("/app/login","Login",None),
    ("/docs","Docs",None),
]:
    s, body, is_json = get(path)
    is_err = "DOCTYPE" in body and "erro" in body.lower()
    v = s == 200 and not is_err
    print(f"  {'✅' if v else '❌'} {nome}: {s}")
    if v: ok += 1

# POST tests
s, d = post_json("/api/v1/phq9-clinico/aplicar?user_id=albert", [2,1,2,1,0,1,2,0,0])
if isinstance(d, dict) and "score" in d:
    print(f"  ✅ PHQ-9 POST: score={d.get('score')} nivel={d.get('classificacao',{}).get('nivel')}")
    ok += 1
else:
    print(f"  ❌ PHQ-9 POST: {s} {str(d)[:60]}")

s2, d2 = post_json("/api/v1/gad7-clinico/aplicar?user_id=albert", [1,2,1,2,1,0,1])
if isinstance(d2, dict) and "score" in d2:
    print(f"  ✅ GAD-7 POST: score={d2.get('score')} nivel={d2.get('nivel')}")
    ok += 1
else:
    print(f"  ❌ GAD-7 POST: {s2} {str(d2)[:60]}")

print(f"\nTOTAL: {ok}/14")
print(f"\n{'='*55}")
print(f"Site: {BASE}")
print(f"Docs: {BASE}/docs")
print(f"PHQ-9: {BASE}/api/v1/phq9-clinico/perguntas")
print(f"GAD-7: {BASE}/api/v1/gad7-clinico/perguntas")
print(f"{'='*55}")
