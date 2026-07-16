#!/usr/bin/env python3
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
    new_content = content[:insert_pos] + "\n" + startup_code + content[insert_pos:]
    
    with open("main.py", "w") as f:
        f.write(new_content)
    print(f"✅ Plugins integrados ao main.py")
    print(f"Novo tamanho: {len(new_content.splitlines())} linhas")
else:
    print("❌ Não encontrou app = FastAPI() no main.py")
