#!/usr/bin/env python3
"""Verifica deploy completo e corrige problemas"""
import os, sys, subprocess

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ {path}")

# ══════════════════════════════════════════════
# 1. Verificar se main.py carrega plugins
# ══════════════════════════════════════════════
print("=== ANALISANDO main.py ===")
with open("main.py") as f:
    main_content = f.read()
    main_lines = main_content.splitlines()

print(f"Linhas: {len(main_lines)}")
print(f"load_all_plugins: {'✅' if 'load_all_plugins' in main_content else '❌'}")
print(f"StaticFiles: {'✅' if 'StaticFiles' in main_content else '❌'}")
print(f"lifespan: {'✅' if 'lifespan' in main_content else '❌'}")
print(f"on_event startup: {'✅' if 'startup' in main_content else '❌'}")

# ══════════════════════════════════════════════
# 2. Criar app_startup.py — ponto de entrada real
# ══════════════════════════════════════════════
w("app_startup.py", '''#!/usr/bin/env python3
"""
app_startup.py — Ponto de entrada principal do Emotion Platform
Carrega main.py + plugins + static files
Use: uvicorn app_startup:app --host 0.0.0.0 --port $PORT
"""
import os
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

logger.info("🚀 Iniciando Emotion Intelligence Platform...")

# 1. Importar app base
from main import app
logger.info("✅ main.py carregado")

# 2. Montar static files
try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
        logger.info("✅ /static montado")
except Exception as e:
    logger.warning(f"Static files: {e}")

# 3. Carregar todos os plugins
try:
    from plugins.loader import load_all_plugins
    ok, err = load_all_plugins(app)
    logger.info(f"✅ {ok} plugins carregados ({err} ignorados)")
    logger.info(f"✅ {len(app.routes)} rotas totais")
except Exception as e:
    logger.error(f"Erro ao carregar plugins: {e}")

logger.info("🎯 Emotion Platform pronto!")
''')

# ══════════════════════════════════════════════
# 3. Atualizar Procfile e render.yaml
# ══════════════════════════════════════════════
w("Procfile", "web: uvicorn app_startup:app --host 0.0.0.0 --port $PORT\n")

w("render.yaml", """services:
  - type: web
    name: emotion-platform-albert
    env: python
    region: oregon
    plan: free
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app_startup:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PORT
        value: "10000"
      - key: PYTHONPATH
        value: "."
      - key: PYTHONUNBUFFERED
        value: "1"
""")

# ══════════════════════════════════════════════
# 4. Verificar requirements.txt
# ══════════════════════════════════════════════
print("\n=== VERIFICANDO REQUIREMENTS ===")
req_path = "requirements.txt"
if os.path.exists(req_path):
    reqs = open(req_path).read()
else:
    reqs = ""

necessarios = {
    "fastapi": "fastapi>=0.104.0",
    "uvicorn": "uvicorn[standard]>=0.24.0",
    "sqlalchemy": "sqlalchemy>=2.0.0",
    "httpx": "httpx>=0.27.0",
    "jinja2": "jinja2>=3.1.0",
    "python-multipart": "python-multipart>=0.0.9",
    "pydantic": "pydantic>=2.0.0",
    "psycopg2": "psycopg2-binary>=2.9.0",
    "aiofiles": "aiofiles>=23.0.0",
    "python-jose": "python-jose[cryptography]>=3.3.0",
    "passlib": "passlib[bcrypt]>=1.7.4",
    "requests": "requests>=2.31.0",
}

adicionados = []
for pkg, spec in necessarios.items():
    if pkg.lower() not in reqs.lower():
        adicionados.append(spec)
        print(f"  ➕ Adicionando: {spec}")
    else:
        print(f"  ✅ Presente: {pkg}")

if adicionados:
    with open(req_path, "a") as f:
        f.write("\n# Adicionados automaticamente\n")
        f.write("\n".join(adicionados) + "\n")
    print(f"\n✅ {len(adicionados)} dependências adicionadas")

# ══════════════════════════════════════════════
# 5. Testar app_startup.py
# ══════════════════════════════════════════════
print("\n=== TESTANDO app_startup.py ===")
try:
    result = subprocess.run(
        [sys.executable, "-c", """
import sys
sys.path.insert(0, '.')
from app_startup import app
from fastapi.testclient import TestClient
client = TestClient(app)

testes = [
    ('GET', '/health', None),
    ('GET', '/api/v1/phq9/perguntas', None),
    ('GET', '/api/v1/chat-ia/modelos/disponiveis', None),
    ('GET', '/api/v1/diario-emocional/emocoes/disponiveis', None),
    ('GET', '/api/v1/agenda-real/disponibilidade/terapeuta123', None),
]

ok = 0
for method, path, body in testes:
    try:
        r = client.get(path)
        status = '✅' if r.status_code < 400 else '❌'
        print(f'{status} {method} {path} → {r.status_code}')
        if r.status_code < 400:
            ok += 1
    except Exception as e:
        print(f'❌ {path}: {e}')

print(f'\\nResultado: {ok}/{len(testes)} endpoints OK')
print(f'Rotas totais: {len(app.routes)}')
"""],
        capture_output=True, text=True, timeout=60
    )
    print(result.stdout)
    if result.stderr:
        erros = [l for l in result.stderr.split('\n') if 'ERROR' in l or 'error' in l.lower()][:5]
        for e in erros:
            print(f"  ⚠️ {e}")
except Exception as e:
    print(f"Teste falhou: {e}")

print("\n" + "="*55)
print("RESUMO")
print("="*55)
print("  ✅ app_startup.py — ponto de entrada")
print("  ✅ Procfile atualizado")
print("  ✅ render.yaml atualizado")
print("  ✅ requirements.txt verificado")
print()
print("  COMANDO RENDER:")
print("  uvicorn app_startup:app --host 0.0.0.0 --port $PORT")
print("="*55)
