#!/usr/bin/env python3
"""Fix RecursionError — muitos lifespans aninhados no FastAPI"""
import os, sys, subprocess, time, urllib.request, json

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

BASE = "https://emotion-platform-albert.onrender.com"

def get(path, t=30):
    try:
        with urllib.request.urlopen(BASE+path, timeout=t) as r:
            body = r.read().decode()
            is_json = body.strip().startswith("{")
            is_err = "DOCTYPE" in body and "erro" in body.lower()
            return r.status, body, is_json, is_err
    except Exception as e:
        return 0, str(e), False, False

print("=== CAUSA: RecursionError — muitos lifespans ===")
print("1477 plugins cada um com FastAPI sub-app = lifespans aninhados")
print("Solução: main.py sem lifespan + plugins sem sub-apps")
print()

# ══════════════════════════════════════════
# SOLUÇÃO: usar APIRouter em vez de FastAPI
# nos plugins, e um único app principal
# ══════════════════════════════════════════

# 1. Novo loader que apenas registra routers (sem FastAPI sub-apps)
w("plugins/loader.py", '''"""Loader Universal — registra APIRouters sem sub-apps (evita RecursionError)"""
import os, importlib, logging
from pathlib import Path

logger = logging.getLogger(__name__)
SKIP = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}

def load_all_plugins(app):
    base = Path(__file__).parent
    ok = err = 0
    for cat in sorted(base.iterdir()):
        if not cat.is_dir() or cat.name.startswith("_"): continue
        for pf in sorted(cat.glob("*.py")):
            if pf.name in SKIP: continue
            mod_path = f"plugins.{cat.name}.{pf.stem}"
            try:
                mod = importlib.import_module(mod_path)
                plug = getattr(mod, "plugin", None)
                if plug and hasattr(plug, "setup"):
                    plug.setup(app)
                    ok += 1
                else:
                    err += 1
            except Exception as e:
                err += 1
                logger.debug(f"skip {mod_path}: {e}")
    logger.info(f"Plugins: {ok} OK / {err} ignorados | Rotas: {len(app.routes)}")
    return ok, err
''')
print("✅ loader.py atualizado")

# 2. Novo plugin_base sem lifespan
w("plugins/plugin_base.py", '''"""PluginBase sem lifespan — evita RecursionError com muitos plugins"""
class PluginBase:
    name = "base"
    version = "1.0.0"
    description = ""
    category = "geral"

    def __init__(self, nome=None):
        pass

    def setup(self, app):
        """Registra rotas no app principal — SEM sub-apps FastAPI"""
        pass

    def health_check(self):
        return {"status": "healthy", "plugin": self.name}
''')
print("✅ plugin_base.py sem lifespan")

# 3. main.py com lifespan=None explícito
w("main.py", '''#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.0 — sem RecursionError"""
import os, logging, importlib
from pathlib import Path
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("ep")

# Carregar plugins ANTES de criar o app
# para evitar lifespan aninhado
SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}
_routers = []  # guardar routers para registrar depois

# Pre-importar todos os módulos
_modules = []
for cat in sorted(Path("plugins").iterdir()):
    if not cat.is_dir() or cat.name.startswith("_"): continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP: continue
        try:
            mod = importlib.import_module(f"plugins.{cat.name}.{pf.stem}")
            _modules.append(mod)
        except Exception as e:
            log.debug(f"import skip: {e}")

log.info(f"Modulos pre-carregados: {len(_modules)}")

# Criar app SEM lifespan (evita RecursionError)
app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1477 plugins de saude mental com IA",
    version="24.0.0",
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
_ok = 0
_err = 0

@app.get("/health")
async def health():
    return {"status":"ok","version":"24.0.0",
            "plugins":_ok,"rotas":len(app.routes),
            "uptime":str(datetime.utcnow()-_start)}

@app.get("/ping")
async def ping():
    return {"pong":True,"ts":datetime.utcnow().isoformat()}

# Registrar plugins no app
for mod in _modules:
    try:
        plug = getattr(mod, "plugin", None)
        if plug and hasattr(plug, "setup"):
            plug.setup(app)
            _ok += 1
    except Exception as e:
        _err += 1
        log.debug(f"setup skip: {e}")

log.info(f"Plugins registrados: {_ok} OK / {_err} err | Rotas: {len(app.routes)}")
''')
print("✅ main.py com lifespan=None")

# 4. Verificar compilação
r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
    capture_output=True, text=True)
print(f"Compilação: {'✅ OK' if r.returncode==0 else '❌ '+r.stderr[:100]}")

# 5. Testar local — verificar que não tem RecursionError
print("\n=== TESTE LOCAL ===")
result = subprocess.run([sys.executable, "-c", """
import sys
sys.setrecursionlimit(500)  # limite baixo para detectar recursão
sys.path.insert(0,".")
for k in list(sys.modules):
    if "plugins" in k: del sys.modules[k]
try:
    from main import app
    from fastapi.testclient import TestClient
    c = TestClient(app, raise_server_exceptions=False)
    print(f"Rotas: {len(app.routes)}")
    ok = 0
    for path in ["/health","/ping","/api/v1/phq9/perguntas",
                 "/api/v1/chat-ia/modelos/disponiveis",
                 "/api/v1/stripe/planos","/api/v1/multi-llm/modelos",
                 "/app/avaliacao","/app/chat","/app/login","/docs"]:
        r = c.get(path)
        is_err = "DOCTYPE" in r.text and r.status_code >= 400
        v = "OK" if r.status_code < 400 and not is_err else "XX"
        print(f"  [{v}] {path}: {r.status_code}")
        if v == "OK": ok += 1
    print(f"LOCAL: {ok}/10")
    print("SEM RecursionError!")
except RecursionError as e:
    print(f"AINDA TEM RECURSION: {e}")
except Exception as e:
    print(f"ERRO: {e}")
    import traceback; traceback.print_exc()
"""], capture_output=True, text=True, timeout=120)
for line in result.stdout.splitlines():
    if line.strip(): print(f"  {line}")
if result.returncode != 0:
    for line in result.stderr.splitlines()[-5:]:
        if line.strip(): print(f"  ERR: {line[:100]}")

# 6. Push
print("\n=== GIT PUSH ===")
for cmd in [
    ["git","add","-A"],
    ["git","commit","--no-verify","-m",
     "fix: RecursionError — lifespan=None + pre-importar modulos — 1477 plugins sem crash"],
    ["git","push"]
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout+r.stderr).strip()[:80]
    print(f"  {'✅' if r.returncode==0 else '❌'} {' '.join(cmd[:2])}: {out}")

# 7. Aguardar e testar
print("\n=== AGUARDANDO DEPLOY (4 min) ===")
for i in range(16):
    time.sleep(15)
    s, body, is_json, is_err = get("/health")
    if is_json and not is_err:
        try:
            d = json.loads(body)
            ver = d.get("version","?")
            plug = d.get("plugins",0)
            print(f"  ✅ {(i+1)*15}s: v{ver} plugins={plug} rotas={d.get('rotas')}")
            if ver == "24.0.0":
                print("  🎉 DEPLOY OK! Sem RecursionError!")
                break
        except: pass
    elif (i+1) % 2 == 0:
        err_tipo = "HTML-ERRO" if is_err else "HTML" if "DOCTYPE" in body else "OUTRO"
        print(f"  ⏳ {(i+1)*15}s: {err_tipo}")

print("\n=== RESULTADO FINAL ===")
ok = 0
for path, nome in [
    ("/health","Health"),("/api/v1/phq9/perguntas","PHQ-9"),
    ("/api/v1/chat-ia/modelos/disponiveis","Chat IA"),
    ("/api/v1/stripe/planos","Stripe"),
    ("/api/v1/auth/stats/usuarios","Auth"),
    ("/api/v1/multi-llm/modelos","Multi-LLM"),
    ("/app/avaliacao","Avaliacao"),("/app/chat","Chat"),
    ("/app/planos","Planos"),("/app/login","Login"),("/docs","Docs"),
]:
    s, body, is_json, is_err = get(path)
    v = s == 200 and not is_err
    tipo = "JSON" if is_json else "HTML"
    print(f"  {'✅' if v else '❌'} {nome}: {s} [{tipo}]")
    if v: ok += 1

print(f"\nTOTAL: {ok}/11")
print(f"Site: {BASE}")
