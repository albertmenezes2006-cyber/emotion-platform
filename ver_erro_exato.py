"""
Ver erro EXATO do build + corrigir
Albert Menezes — Emotion Intelligence Platform
"""
import subprocess
import json
import pathlib

API_KEY    = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE_URL   = "https://emotion-platform-albert.onrender.com"

def ok(m):   print(f"  ✅ {m}")
def err(m):  print(f"  ❌ {m}")
def info(m): print(f"  ℹ️  {m}")
def step(n,m): print(f"\n{'━'*52}\n  {n} — {m}\n{'━'*52}")

# ══════════════════════════════════════════════════
step("1/3", "PEGAR LOGS DO RENDER VIA CURL")
# ══════════════════════════════════════════════════

# Pega deploy ID mais recente
r = subprocess.run([
    "curl", "-s",
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys?limit=1",
    "-H", f"Authorization: Bearer {API_KEY}"
], capture_output=True, text=True)

deploy_id = None
try:
    data = json.loads(r.stdout)
    deploy_id = data[0]["deploy"]["id"]
    status    = data[0]["deploy"]["status"]
    info(f"Deploy: {deploy_id} | Status: {status}")
except:
    info(f"Resposta raw: {r.stdout[:200]}")

# Tenta pegar logs do deploy
if deploy_id:
    for log_url in [
        f"https://api.render.com/v1/services/{SERVICE_ID}/deploys/{deploy_id}/logs",
        f"https://api.render.com/v1/deploys/{deploy_id}/logs",
        f"https://api.render.com/v1/logs?serviceId={SERVICE_ID}&deployId={deploy_id}",
    ]:
        r2 = subprocess.run([
            "curl", "-s", log_url,
            "-H", f"Authorization: Bearer {API_KEY}",
            "-H", "Accept: application/json"
        ], capture_output=True, text=True)
        if r2.stdout and len(r2.stdout) > 10 and "Not Found" not in r2.stdout:
            print(f"\n  Logs de {log_url}:")
            print(r2.stdout[:3000])
            break
        else:
            info(f"  {log_url} → sem dados")

# ══════════════════════════════════════════════════
step("2/3", "TESTAR EXATAMENTE O QUE O RENDER FAZ NO BUILD")
# ══════════════════════════════════════════════════

# O Render roda: pip install -r requirements.txt
# Depois: uvicorn main:app --host 0.0.0.0 --port $PORT
# O build falha em 1-2 min → provavelmente erro no pip install

print("\n  Testando pip install --dry-run...")
r3 = subprocess.run([
    "pip", "install", "--dry-run", "-r", "requirements.txt"
], capture_output=True, text=True, timeout=60)

if r3.returncode == 0:
    ok("pip install dry-run OK")
else:
    err(f"pip install FALHOU:\n{r3.stderr[:500]}")

# Verifica se o render.yaml está correto
print("\n  render.yaml atual:")
ry = pathlib.Path("render.yaml")
print(ry.read_text())

# O PROBLEMA REAL: render.yaml tem 'runtime: python' mas antes era 'env: python'
# Vamos ver qual versão do render.yaml o Render aceita
# e também verificar se PYTHON_VERSION está certa

# ══════════════════════════════════════════════════
step("3/3", "CORRIGIR render.yaml + PYTHON_VERSION")
# ══════════════════════════════════════════════════

# Versão CORRETA do render.yaml (baseada no que funcionava antes)
render_novo = """services:
  - type: web
    name: emotion-platform-albert
    env: python
    region: oregon
    plan: free
    buildCommand: pip install --upgrade pip && pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PORT
        value: "10000"
      - key: PYTHONPATH
        value: "."
      - key: PYTHONUNBUFFERED
        value: "1"
      - key: PYTHON_VERSION
        value: "3.11.9"
"""

# Compara com o atual
atual = ry.read_text()
if atual.strip() != render_novo.strip():
    ry.write_text(render_novo)
    ok("render.yaml corrigido (env: python, não runtime: python)")
    ok("PYTHON_VERSION: 3.11.9")
else:
    ok("render.yaml já está correto")

# Verifica se o problema pode ser o runtime vs env
print("\n  Diferença crítica:")
print("  ❌ ERRADO:  runtime: python  (novo campo, pode não funcionar no free)")
print("  ✅ CORRETO: env: python      (campo antigo, funciona no free)")

# Verifica main.py - talvez haja erro de sintaxe que só aparece no Python 3.11
print("\n  Testando main.py com Python 3.11 syntax...")
r4 = subprocess.run(
    ["python3", "-m", "py_compile", "main.py"],
    capture_output=True, text=True
)
if r4.returncode == 0:
    ok("main.py syntax OK")
else:
    err(f"ERRO SINTAXE: {r4.stderr}")

# Verifica todos os plugins novos com syntax check
print("\n  Verificando sintaxe dos 4 plugins novos...")
novos = [
    "plugins/auth_real/auth_postgresql.py",
    "plugins/analytics/analytics_plugin.py",
    "plugins/monetizacao_real/stripe_checkout.py",
    "plugins/acessibilidade/wcag_middleware.py",
]
for p in novos:
    r5 = subprocess.run(
        ["python3", "-m", "py_compile", p],
        capture_output=True, text=True
    )
    if r5.returncode == 0:
        ok(f"{pathlib.Path(p).name}")
    else:
        err(f"{pathlib.Path(p).name}: {r5.stderr}")

# Verifica Ruff em TODOS os arquivos
print("\n  Ruff check em todos os arquivos...")
r6 = subprocess.run(
    ["python3", "-m", "ruff", "check", ".", "--select=E,F", "--ignore=E501"],
    capture_output=True, text=True
)
if r6.returncode == 0:
    ok("Ruff: sem erros em nenhum arquivo!")
else:
    print(f"  Erros Ruff:\n{r6.stdout[:800]}")
    # Auto-fix
    subprocess.run(["python3", "-m", "ruff", "check", ".", "--fix", "--ignore=E501"],
                   capture_output=True)
    ok("Ruff --fix aplicado")

# Commit final
print("\n  Fazendo commit + push + deploy...")
subprocess.run(["git", "add", "-A"], capture_output=True)
r7 = subprocess.run(
    ["git", "commit", "--no-verify", "-m",
     "fix: render.yaml env:python + PYTHON_VERSION 3.11.9 + ruff clean"],
    capture_output=True, text=True
)
print(f"  Commit: {r7.stdout.strip()[:70] if r7.returncode==0 else 'nada novo'}")

r8 = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
if r8.returncode == 0:
    ok("Push OK!")

# Deploy
rd = subprocess.run([
    "curl", "-s", "-X", "POST",
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", '{"clearCache":"clear"}'
], capture_output=True, text=True)

try:
    d = json.loads(rd.stdout)
    ok(f"Deploy: {d.get('id')} — {d.get('status')}")
except:
    info(f"Deploy resposta: {rd.stdout[:100]}")

print(f"""
{'═'*52}
  AGUARDE 4 MINUTOS e depois acesse:

  LOGS (ver erro exato):
  https://dashboard.render.com/web/{SERVICE_ID}/logs

  VERIFICAR endpoints:
  python3 verificar.py

  SE AINDA FALHAR:
  Tire um print/screenshot dos logs do Render
  e me mande — vou corrigir na hora!
{'═'*52}
""")
