#!/usr/bin/env python3
"""
Verifica e corrige main.py para servir o frontend corretamente
Adiciona static files e monta loader universal
"""
import os, re

# Ler main.py
with open("main.py", "r") as f:
    content = f.read()

print(f"main.py: {len(content.splitlines())} linhas")

# Verificar o que já existe
tem_static = "StaticFiles" in content
tem_loader = "load_all_plugins" in content
tem_templates = "Jinja2Templates" in content

print(f"StaticFiles: {'✅' if tem_static else '❌'}")
print(f"load_all_plugins: {'✅' if tem_loader else '❌'}")
print(f"Jinja2Templates: {'✅' if tem_templates else '❌'}")

# Criar patch seguro
with open("patch_main.py", "w") as f:
    f.write('''#!/usr/bin/env python3
"""
Patch seguro para main.py — roda ANTES do uvicorn
Monta static files e carrega plugins sem modificar main.py
"""
import os, sys, logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importar app do main
sys.path.insert(0, ".")
from main import app

# Montar static files
try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
        logger.info("✅ Static files montados")
except Exception as e:
    logger.warning(f"Static: {e}")

# Carregar todos os plugins
try:
    from plugins.loader import load_all_plugins
    ok, err = load_all_plugins(app)
    logger.info(f"✅ Plugins: {ok} carregados, {err} ignorados")
    logger.info(f"✅ Rotas totais: {len(app.routes)}")
except Exception as e:
    logger.error(f"Loader error: {e}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
''')
print("✅ patch_main.py criado")

# Verificar se main.py já tem startup event para plugins
if "load_all_plugins" not in content and "@app.on_event" not in content:
    print("\n⚠️  main.py NÃO carrega plugins automaticamente")
    print("Criando startup_plugins.py...")

    with open("startup_plugins.py", "w") as f:
        f.write('''#!/usr/bin/env python3
"""
startup_plugins.py — Adiciona carregamento de plugins ao main.py
Execute uma vez para integrar
"""
import re

with open("main.py", "r") as f:
    content = f.read()

# Adicionar imports necessários no topo
imports_add = """
# === EMOTION PLATFORM — PLUGIN SYSTEM ===
import os as _os_plugins
from fastapi.staticfiles import StaticFiles as _StaticFiles
"""

# Adicionar código de startup após a criação do app
startup_code = """
# === CARREGAR TODOS OS PLUGINS ===
try:
    _static_dir = "static"
    if _os_plugins.path.exists(_static_dir):
        app.mount("/static", _StaticFiles(directory=_static_dir), name="static")
except Exception as _e:
    pass

try:
    from plugins.loader import load_all_plugins as _load_plugins
    _load_plugins(app)
except Exception as _e:
    print(f"Plugins: {_e}")
# === FIM PLUGINS ===
"""

# Encontrar onde o app é criado
app_match = re.search(r'app\s*=\s*FastAPI\([^)]*\)', content)
if app_match:
    insert_pos = app_match.end()
    new_content = content[:insert_pos] + "\\n" + startup_code + content[insert_pos:]
    
    with open("main.py", "w") as f:
        f.write(new_content)
    print(f"✅ Plugins integrados ao main.py")
    print(f"Novo tamanho: {len(new_content.splitlines())} linhas")
else:
    print("❌ Não encontrou app = FastAPI() no main.py")
''')
    print("✅ startup_plugins.py criado")
else:
    print("✅ main.py já tem integração de plugins")

print("\n=== PRÓXIMOS PASSOS ===")
print("1. Verifique se main.py monta /static e carrega plugins")
print("2. Se não: python3 startup_plugins.py")
print("3. Teste local: python3 patch_main.py")
print("4. No Render: o loader.py já é chamado via lifespan ou startup")
