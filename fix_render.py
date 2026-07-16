#!/usr/bin/env python3
"""Corrige o startup do Render — integra plugins direto no main.py de forma segura"""
import os, re

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ {path}")

# ══════════════════════════════════════════════
# 1. Ler main.py e encontrar onde injetar
# ══════════════════════════════════════════════
with open("main.py") as f:
    content = f.read()
    lines = content.splitlines()

print(f"main.py: {len(lines)} linhas")

# Verificar se já tem o loader
if "load_all_plugins" in content:
    print("✅ load_all_plugins já está no main.py")
else:
    print("❌ Precisa injetar loader no main.py")

    # Encontrar a linha com app = FastAPI(
    app_line_idx = None
    for i, line in enumerate(lines):
        if re.search(r'app\s*=\s*FastAPI\s*\(', line):
            app_line_idx = i
            print(f"  app = FastAPI() encontrado na linha {i+1}")
            break

    if app_line_idx is not None:
        # Encontrar o fechamento do FastAPI(...)
        depth = 0
        end_idx = app_line_idx
        for i in range(app_line_idx, min(app_line_idx + 20, len(lines))):
            depth += lines[i].count('(') - lines[i].count(')')
            if depth <= 0:
                end_idx = i
                break

        # Código a injetar APÓS app = FastAPI(...)
        inject_code = """

# ═══════════════════════════════════════════════
# EMOTION PLATFORM — PLUGIN SYSTEM AUTO-LOAD
# ═══════════════════════════════════════════════
import os as _os_ep
try:
    from fastapi.staticfiles import StaticFiles as _SF_ep
    if _os_ep.path.exists("static"):
        app.mount("/static", _SF_ep(directory="static"), name="static")
except Exception as _e_sf:
    pass

try:
    from plugins.loader import load_all_plugins as _lap_ep
    _lap_ep(app)
except Exception as _e_pl:
    import logging as _lg_ep
    _lg_ep.getLogger(__name__).error(f"Plugin loader: {_e_pl}")
# ═══════════════════════════════════════════════
"""
        # Inserir após a linha de fechamento
        new_lines = lines[:end_idx+1] + inject_code.splitlines() + lines[end_idx+1:]
        new_content = "\n".join(new_lines)

        # Backup
        with open("main.py.bak", "w") as f:
            f.write(content)
        print("✅ Backup em main.py.bak")

        # Salvar
        with open("main.py", "w") as f:
            f.write(new_content)
        print(f"✅ main.py atualizado: {len(new_content.splitlines())} linhas")
    else:
        print("❌ Não encontrou app = FastAPI() — injeção manual necessária")

# ══════════════════════════════════════════════
# 2. Verificar se main.py compila
# ══════════════════════════════════════════════
import subprocess, sys
result = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
                       capture_output=True, text=True)
if result.returncode == 0:
    print("✅ main.py compila OK")
else:
    print("❌ ERRO DE COMPILAÇÃO — restaurando backup")
    os.rename("main.py.bak", "main.py")
    print(result.stderr[:200])

# ══════════════════════════════════════════════
# 3. Procfile correto
# ══════════════════════════════════════════════
w("Procfile", "web: uvicorn main:app --host 0.0.0.0 --port $PORT\n")
print("✅ Procfile: uvicorn main:app")

# ══════════════════════════════════════════════
# 4. render.yaml correto
# ══════════════════════════════════════════════
w("render.yaml", """services:
  - type: web
    name: emotion-platform-albert
    env: python
    region: oregon
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PORT
        value: "10000"
      - key: PYTHONPATH
        value: "."
      - key: PYTHONUNBUFFERED
        value: "1"
""")

# ══════════════════════════════════════════════
# 5. Testar se funciona
# ══════════════════════════════════════════════
print("\n=== TESTANDO IMPORTAÇÃO ===")
result2 = subprocess.run(
    [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from main import app
print(f'✅ app importado: {type(app).__name__}')
print(f'✅ Rotas: {len(app.routes)}')

# Verificar rotas importantes
paths = [r.path for r in app.routes if hasattr(r, 'path')]
has_health = '/health' in paths
has_phq9 = any('phq9' in p for p in paths)
has_chat = any('chat-ia' in p for p in paths)
has_home = '/' in paths
print(f'  / (home): {"✅" if has_home else "❌"}')
print(f'  /health: {"✅" if has_health else "❌"}')
print(f'  /api/v1/phq9/*: {"✅" if has_phq9 else "❌"}')
print(f'  /api/v1/chat-ia/*: {"✅" if has_chat else "❌"}')
"""],
    capture_output=True, text=True, timeout=60
)
print(result2.stdout)
if result2.returncode != 0:
    erros = [l for l in result2.stderr.split('\n') if l.strip() and 'warning' not in l.lower()][:10]
    for e in erros:
        print(f"  ⚠️ {e}")

print("="*50)
