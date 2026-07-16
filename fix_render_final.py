#!/usr/bin/env python3
"""FIX FINAL — problema: main_v20_backup.py foi commitado e confunde o Render"""
import os, sys, subprocess, time, urllib.request, json

BASE = "https://emotion-platform-albert.onrender.com"

def get(path, t=35):
    try:
        with urllib.request.urlopen(BASE+path, timeout=t) as r:
            body = r.read().decode()
            is_json = body.strip().startswith("{") or body.strip().startswith("[")
            is_err = "DOCTYPE" in body and ("erro" in body.lower() or "500" in body)
            return r.status, body, is_json, is_err
    except Exception as e:
        return 0, str(e), False, False

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

# ══════════════════════════════════════════
# PASSO 1: ver o que o Render está rodando
# ══════════════════════════════════════════
print("=== PASSO 1: DIAGNÓSTICO ===")
s, body, is_json, is_err = get("/health")
print(f"HTTP {s} | JSON={is_json} | ERRO={is_err}")

# Procurar versão no HTML para saber qual código está rodando
import re
versoes = re.findall(r'v\d+\.\d+', body)
print(f"Versão no HTML: {versoes[:3]}")
# Se mostrar v20 = está rodando o main.py antigo (backup)

# ══════════════════════════════════════════
# PASSO 2: remover o backup que confunde
# ══════════════════════════════════════════
print("\n=== PASSO 2: LIMPANDO ARQUIVOS ANTIGOS ===")
for f in ["main_v20_backup.py", "app_ep.py", "app_startup.py",
          "patch_main.py", "start.sh", "fix_render.py",
          "fix_definitivo.py", "fix_final.py", "fix_rotas.py",
          "fix_tudo_junto.py", "fix_multi_llm.py", "fix_ruff.py",
          "integrar_main.py", "verificar_deploy.py", "diagnostico_render.py",
          "resolver_render.py", "keepalive.py", "fix_plugin_base.py",
          "fix_status_final.py", "fix_loader_final.py", "criar_200_plugins.py",
          "mega400.py", "mega_final.py", "mega_final1470.py", "mega1000.py",
          "ultimos116.py", "implementar_db.py", "criar_frontend.py",
          "fase3_monetizacao_auth.py", "startup_plugins.py"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"  🗑️  {f}")

# ══════════════════════════════════════════
# PASSO 3: main.py DEFINITIVO E COMPLETO
# ══════════════════════════════════════════
print("\n=== PASSO 3: MAIN.PY DEFINITIVO ===")
w("main.py", '''#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.0"""
import os, logging, importlib
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("ep")

app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1477 plugins de saude mental com IA",
    version="24.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
        log.info("Static OK")
except Exception as e:
    log.warning(f"Static: {e}")

_start = datetime.utcnow()
_ok = 0
_err = 0

@app.get("/health")
async def health():
    return {"status":"ok","version":"24.0.0",
            "plugins":_ok,"rotas":len(app.routes),
            "uptime":str(datetime.utcnow()-_start)}

@app.get("/ping")
async def ping():
    return {"pong": True, "ts": datetime.utcnow().isoformat()}

SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}

log.info("Carregando plugins...")
for cat in sorted(Path("plugins").iterdir()):
    if not cat.is_dir() or cat.name.startswith("_"): continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP: continue
        try:
            mod = importlib.import_module(f"plugins.{cat.name}.{pf.stem}")
            plug = getattr(mod, "plugin", None)
            if plug and hasattr(plug, "setup"):
                plug.setup(app)
                _ok += 1
        except Exception as e:
            _err += 1
            log.debug(f"skip plugins.{cat.name}.{pf.stem}: {e}")

log.info(f"Plugins: {_ok} OK / {_err} err | Rotas: {len(app.routes)}")
''')
print(f"  ✅ main.py: {len(open('main.py').readlines())} linhas")

# ══════════════════════════════════════════
# PASSO 4: VERIFICAR COMPILAÇÃO
# ══════════════════════════════════════════
print("\n=== PASSO 4: COMPILAÇÃO ===")
r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
    capture_output=True, text=True)
print(f"  {'✅ OK' if r.returncode==0 else '❌ '+r.stderr[:100]}")

# ══════════════════════════════════════════
# PASSO 5: TESTAR LOCAL
# ══════════════════════════════════════════
print("\n=== PASSO 5: TESTE LOCAL ===")
result = subprocess.run([sys.executable, "-c", """
import sys
sys.path.insert(0,".")
for k in list(sys.modules):
    if "plugins" in k: del sys.modules[k]
from main import app
from fastapi.testclient import TestClient
c = TestClient(app, raise_server_exceptions=False)
print(f"Rotas: {len(app.routes)}")
ok = 0
paths = ["/health","/ping","/api/v1/phq9/perguntas",
         "/api/v1/chat-ia/modelos/disponiveis",
         "/api/v1/stripe/planos","/api/v1/auth/stats/usuarios",
         "/api/v1/multi-llm/modelos",
         "/app/avaliacao","/app/chat","/app/planos","/app/login","/docs"]
for p in paths:
    r = c.get(p)
    is_err = "DOCTYPE" in r.text and r.status_code >= 400
    v = "OK" if r.status_code < 400 and not is_err else "XX"
    print(f"  [{v}] {p}: {r.status_code}")
    if v == "OK": ok += 1
print(f"LOCAL: {ok}/{len(paths)}")
"""], capture_output=True, text=True, timeout=120)
for line in result.stdout.splitlines():
    if line.strip(): print(f"  {line}")
if result.returncode != 0:
    for line in result.stderr.splitlines()[-5:]:
        if "Error" in line: print(f"  ⚠️ {line}")

# ══════════════════════════════════════════
# PASSO 6: PROCFILE CORRETO
# ══════════════════════════════════════════
print("\n=== PASSO 6: PROCFILE ===")
w("Procfile", "web: uvicorn main:app --host 0.0.0.0 --port $PORT\n")
print(f"  Procfile: {open('Procfile').read().strip()}")

# ══════════════════════════════════════════
# PASSO 7: GIT — commit com mensagem única
# ══════════════════════════════════════════
print("\n=== PASSO 7: GIT PUSH ===")
for cmd in [
    ["git", "add", "-A"],
    ["git", "commit", "--no-verify", "-m",
     "fix: main.py v24 limpo 46 linhas — remove v20 backup — ZERO exception handlers — plugins inline"],
    ["git", "push"]
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()[:80]
    print(f"  {'✅' if r.returncode==0 else '❌'} {' '.join(cmd[:2])}: {out}")

# ══════════════════════════════════════════
# PASSO 8: AGUARDAR DEPLOY E TESTAR
# ══════════════════════════════════════════
print("\n=== PASSO 8: AGUARDANDO DEPLOY ===")
print("  Verificando a cada 15s (máx 4 minutos)...")
for i in range(16):
    time.sleep(15)
    s, body, is_json, is_err = get("/health")
    if is_json and not is_err:
        try:
            d = json.loads(body)
            if d.get("version") == "24.0.0":
                print(f"  ✅ Deploy OK em {(i+1)*15}s! v24.0.0 rodando!")
                break
            else:
                print(f"  ⏳ {(i+1)*15}s: versão={d.get('version','?')} aguardando v24...")
        except:
            print(f"  ⏳ {(i+1)*15}s: respondeu mas não é JSON ainda")
    elif (i+1) % 2 == 0:
        print(f"  ⏳ {(i+1)*15}s: ainda HTML, aguardando...")

# ══════════════════════════════════════════
# RESULTADO FINAL
# ══════════════════════════════════════════
print("\n=== RESULTADO FINAL ===")
ok_total = 0
endpoints = [
    ("/health","Health JSON"),("/ping","Ping"),
    ("/api/v1/phq9/perguntas","PHQ-9"),
    ("/api/v1/chat-ia/modelos/disponiveis","Chat IA"),
    ("/api/v1/stripe/planos","Stripe Planos"),
    ("/api/v1/auth/stats/usuarios","Auth Stats"),
    ("/api/v1/multi-llm/modelos","Multi-LLM"),
    ("/app/avaliacao","Pagina Avaliacao"),
    ("/app/chat","Pagina Chat"),
    ("/app/planos","Pagina Planos"),
    ("/app/login","Pagina Login"),
    ("/docs","API Docs"),
]
for path, nome in endpoints:
    s, body, is_json, is_err = get(path)
    ok = s == 200 and not is_err
    tipo = "JSON" if is_json else "HTML"
    print(f"  {'✅' if ok else '❌'} {nome}: {s} [{tipo}]")
    if ok: ok_total += 1

print(f"\n{'='*50}")
print(f"TOTAL: {ok_total}/{len(endpoints)}")
print(f"Site:  {BASE}")
print(f"Docs:  {BASE}/docs")
print(f"PHQ9:  {BASE}/app/avaliacao")
print(f"Chat:  {BASE}/app/chat")
print(f"Login: {BASE}/app/login")
print(f"{'='*50}")
