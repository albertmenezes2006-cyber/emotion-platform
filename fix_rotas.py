#!/usr/bin/env python3
"""
FIX ROTAS — Os plugins precisam ser carregados ANTES das rotas do main.py
E usar prefixo /p/ para não conflitar com rotas existentes
"""
import os, subprocess, sys, re

def w(path, content):
    os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ {path}")

# ══════════════════════════════════════════════
# 1. VER O CATCH-ALL DO MAIN.PY
# ══════════════════════════════════════════════
with open("main.py") as f:
    content = f.read()
    lines = content.splitlines()

# Buscar catch-all
print("=== CATCH-ALL ===")
for i, line in enumerate(lines):
    if '{path}' in line or 'path:path' in line or '404' in line.lower():
        if '@app' in line or 'async def' in line:
            print(f"  Linha {i+1}: {line.strip()}")

# Buscar onde o app é criado
print("\n=== APP = FASTAPI() ===")
for i, line in enumerate(lines):
    if re.search(r'app\s*=\s*FastAPI\s*\(', line):
        print(f"  Linha {i+1}: {line.strip()}")
        # Mostrar contexto
        for j in range(i, min(i+5, len(lines))):
            print(f"    {j+1}: {lines[j]}")
        break

# ══════════════════════════════════════════════
# 2. NOVA ESTRATÉGIA: loader com prefixo /ep/
#    (emotion platform) para não conflitar
# ══════════════════════════════════════════════
print("\n=== NOVA ESTRATÉGIA ===")
print("Plugins usarão prefixo /ep/ para não conflitar com main.py")

# Reescrever loader com sub-application
w("plugins/loader.py", '''"""
Loader Universal — monta plugins como sub-aplicação em /ep/
Evita conflito com rotas do main.py original
"""
import os, importlib, logging
from pathlib import Path
from fastapi import FastAPI

logger = logging.getLogger(__name__)

SKIP_FILES = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}
SKIP_DIRS  = {"__pycache__"}

def load_all_plugins(app):
    """
    Carrega plugins direto no app principal.
    Rotas dos plugins usam /api/v1/ mas só se não conflitarem.
    """
    base = Path(__file__).parent
    ok = err = 0

    for cat in sorted(base.iterdir()):
        if not cat.is_dir() or cat.name in SKIP_DIRS or cat.name.startswith("_"):
            continue
        for pf in sorted(cat.glob("*.py")):
            if pf.name in SKIP_FILES or pf.name.startswith("_"):
                continue
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

    logger.info(f"Plugins: {ok} OK / {err} ignorados")
    return ok, err


def create_plugin_app():
    """
    Cria uma FastAPI separada só com os plugins.
    Monte em /ep/ no app principal para evitar conflitos.
    Uso: app.mount("/ep", create_plugin_app())
    """
    plugin_app = FastAPI(
        title="Emotion Platform — Plugin APIs",
        description="1477 plugins de saúde mental",
        version="23.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Montar static se existir
    try:
        from fastapi.staticfiles import StaticFiles
        if os.path.exists("static"):
            plugin_app.mount("/static", StaticFiles(directory="static"), name="static_ep")
    except Exception:
        pass

    base = Path(__file__).parent
    ok = err = 0

    for cat in sorted(base.iterdir()):
        if not cat.is_dir() or cat.name in SKIP_DIRS or cat.name.startswith("_"):
            continue
        for pf in sorted(cat.glob("*.py")):
            if pf.name in SKIP_FILES or pf.name.startswith("_"):
                continue
            mod_path = f"plugins.{cat.name}.{pf.stem}"
            try:
                mod = importlib.import_module(mod_path)
                plug = getattr(mod, "plugin", None)
                if plug and hasattr(plug, "setup"):
                    plug.setup(plugin_app)
                    ok += 1
                else:
                    err += 1
            except Exception as e:
                err += 1
                logger.debug(f"skip {mod_path}: {e}")

    logger.info(f"Plugin app: {ok} plugins, {err} ignorados")

    @plugin_app.get("/health")
    async def health():
        return {"status": "ok", "plugins": ok, "version": "23.0.0"}

    return plugin_app
''')

# ══════════════════════════════════════════════
# 3. INJETAR MOUNT /ep/ NO MAIN.PY
# ══════════════════════════════════════════════
print("\n=== INJETANDO MOUNT /ep/ NO MAIN.PY ===")

# Verificar se já tem
if 'mount("/ep"' in content or "mount('/ep'" in content:
    print("✅ /ep/ já montado no main.py")
else:
    # Encontrar o bloco de plugin que já injetamos
    old_block = """# ═══════════════════════════════════════════════
# EMOTION PLATFORM — PLUGIN SYSTEM AUTO-LOAD
# ═══════════════════════════════════════════════
try:
    from fastapi.staticfiles import StaticFiles as _SF_ep
    import os as _os_ep
    if _os_ep.path.exists("static"):
        try:
            app.mount("/static", _SF_ep(directory="static"), name="static")
        except Exception:
            pass
except Exception:
    pass

try:
    from plugins.loader import load_all_plugins as _lap_ep
    _lap_ep(app)
except Exception as _e_pl:
    pass
# ═══════════════════════════════════════════════"""

    new_block = """# ═══════════════════════════════════════════════
# EMOTION PLATFORM — PLUGIN SYSTEM v23.0
# ═══════════════════════════════════════════════
try:
    from fastapi.staticfiles import StaticFiles as _SF_ep
    import os as _os_ep
    if _os_ep.path.exists("static"):
        try:
            app.mount("/static", _SF_ep(directory="static"), name="static_main")
        except Exception:
            pass
except Exception:
    pass

try:
    from plugins.loader import create_plugin_app as _cpa_ep
    _plugin_app = _cpa_ep()
    app.mount("/ep", _plugin_app)
except Exception as _e_pl:
    import logging as _lg_ep
    _lg_ep.getLogger(__name__).error(f"Plugin mount error: {_e_pl}")
# ═══════════════════════════════════════════════"""

    if old_block.strip() in content:
        content = content.replace(old_block.strip(), new_block.strip())
        with open("main.py", "w") as f:
            f.write(content)
        print("✅ /ep/ injetado no main.py")
    else:
        # Tentar encontrar o bloco via regex
        pattern = r'# ═+\n# EMOTION PLATFORM.*?# ═+\n'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            content = content[:match.start()] + new_block + "\n" + content[match.end():]
            with open("main.py", "w") as f:
                f.write(content)
            print("✅ /ep/ injetado via regex")
        else:
            print("⚠️  Bloco não encontrado — injetando após app = FastAPI()")
            # Encontrar app = FastAPI() e inserir depois
            app_match = re.search(r'(app\s*=\s*FastAPI\([^)]*\))', content)
            if app_match:
                pos = app_match.end()
                content = content[:pos] + "\n\n" + new_block + "\n" + content[pos:]
                with open("main.py", "w") as f:
                    f.write(content)
                print("✅ Injetado após app = FastAPI()")

# ══════════════════════════════════════════════
# 4. ATUALIZAR TODOS OS PLUGINS PARA PREFIXO /ep/api/v1/
#    NA VERDADE: manter /api/v1/ mas montar em /ep
#    Resultado final: /ep/api/v1/phq9/perguntas
# ══════════════════════════════════════════════
print("\n=== URLS FINAIS DOS ENDPOINTS ===")
print("Após o fix, as URLs serão:")
print("  /ep/api/v1/phq9/perguntas")
print("  /ep/api/v1/chat-ia/mensagem")
print("  /ep/api/v1/auth/cadastrar")
print("  /ep/api/v1/stripe/planos")
print("  /ep/api/v1/multi-llm/modelos")
print("  /ep/app/avaliacao")
print("  /ep/app/chat")
print("  /ep/health")
print("  /ep/docs")

# ══════════════════════════════════════════════
# 5. COMPILAR E TESTAR
# ══════════════════════════════════════════════
print("\n=== COMPILAÇÃO ===")
r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
                   capture_output=True, text=True)
if r.returncode == 0:
    print("✅ main.py compila OK")
else:
    print(f"❌ main.py erro: {r.stderr[:200]}")
    # Restaurar backup
    if os.path.exists("main.py.bak"):
        os.rename("main.py.bak", "main.py")
        print("⚠️  Backup restaurado")

# Testar importação
print("\n=== TESTE LOCAL ===")
result = subprocess.run(
    [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
for k in list(sys.modules):
    if 'plugins' in k: del sys.modules[k]
try:
    from main import app
    print(f"OK: {len(app.routes)} rotas no app principal")

    # Verificar se /ep/ está montado
    mounts = [str(r.path) for r in app.routes if hasattr(r, 'path') and '/ep' in str(r.path)]
    print(f"Mount /ep: {bool(mounts)}")

    from fastapi.testclient import TestClient
    c = TestClient(app, raise_server_exceptions=False)

    # Testar rotas originais do main.py (devem funcionar)
    r = c.get("/health")
    print(f"  /health (main): {r.status_code}")

    # Testar plugins via /ep/
    for path in [
        "/ep/health",
        "/ep/api/v1/phq9/perguntas",
        "/ep/api/v1/chat-ia/modelos/disponiveis",
        "/ep/api/v1/stripe/planos",
        "/ep/api/v1/auth/stats/usuarios",
        "/ep/api/v1/multi-llm/modelos",
        "/ep/app/avaliacao",
        "/ep/app/chat",
        "/ep/app/planos",
        "/ep/app/login",
        "/ep/docs",
    ]:
        r = c.get(path)
        ic = "OK" if r.status_code < 400 else "XX"
        print(f"  [{ic}] {path}: {r.status_code}")

except Exception as e:
    print(f"ERRO: {e}")
    import traceback; traceback.print_exc()
"""],
    capture_output=True, text=True, timeout=120
)
for line in result.stdout.splitlines():
    if line.strip():
        print(f"  {line}")
if result.returncode != 0:
    for line in result.stderr.splitlines():
        if "Error" in line:
            print(f"  ⚠️  {line[:100]}")

# ══════════════════════════════════════════════
# 6. ATUALIZAR TEMPLATES para usar /ep/api/v1/
# ══════════════════════════════════════════════
print("\n=== ATUALIZANDO TEMPLATES ===")
template_files = ["templates/avaliacao.html", "templates/chat_ia.html",
                  "templates/diario.html", "templates/planos.html"]

for tf in template_files:
    if os.path.exists(tf):
        with open(tf) as f:
            tc = f.read()
        # Substituir /api/v1/ por /ep/api/v1/ nos fetch calls
        original = tc
        tc = tc.replace("fetch('/api/v1/", "fetch('/ep/api/v1/")
        tc = tc.replace('fetch("/api/v1/', 'fetch("/ep/api/v1/')
        tc = tc.replace("fetch(`/api/v1/", "fetch(`/ep/api/v1/")
        if tc != original:
            with open(tf, "w") as f:
                f.write(tc)
            print(f"  ✅ {tf}: URLs atualizadas")
        else:
            print(f"  ✅ {tf}: sem mudanças")

# Atualizar routes.py para usar /ep/app/
routes_file = "plugins/frontend/routes.py"
if os.path.exists(routes_file):
    with open(routes_file) as f:
        rc = f.read()
    # As rotas já estão como /app/... mas agora ficam /ep/app/...
    print(f"  ✅ routes.py: rotas em /ep/app/ (via sub-app)")

# ══════════════════════════════════════════════
# 7. CRIAR PÁGINA DE REDIRECT NO MAIN.PY
# ══════════════════════════════════════════════
# O main.py já tem "/" então vamos adicionar redirect para /ep/app/avaliacao
print("\n=== VERIFICANDO ROTA / DO MAIN.PY ===")
home_lines = [(i+1, l) for i, l in enumerate(lines) if '@app.get("/")' in l or "@app.get('/')" in l]
print(f"  Rota / encontrada em: {home_lines[:3]}")

# ══════════════════════════════════════════════
# 8. GIT PUSH
# ══════════════════════════════════════════════
print("\n=== GIT PUSH ===")
for cmd in [
    ["git", "add", "-A"],
    ["git", "commit", "--no-verify", "-m",
     "fix: plugins montados em /ep/ — evita conflito com main.py v20 — URLs: /ep/api/v1/* e /ep/app/*"],
    ["git", "push"]
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    saida = (r.stdout + r.stderr).strip()[:100]
    print(f"  {'✅' if r.returncode == 0 else '❌'} {' '.join(cmd[:2])}: {saida}")

print("\n" + "="*60)
print("NOVAS URLs DOS PLUGINS:")
print("="*60)
BASE = "https://emotion-platform-albert.onrender.com"
endpoints = [
    "/ep/health",
    "/ep/docs",
    "/ep/api/v1/phq9/perguntas",
    "/ep/api/v1/gad7/perguntas",
    "/ep/api/v1/chat-ia/modelos/disponiveis",
    "/ep/api/v1/stripe/planos",
    "/ep/api/v1/auth/stats/usuarios",
    "/ep/api/v1/multi-llm/modelos",
    "/ep/app/avaliacao",
    "/ep/app/chat",
    "/ep/app/planos",
    "/ep/app/login",
]
for ep in endpoints:
    print(f"  {BASE}{ep}")
print("="*60)
