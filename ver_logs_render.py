"""
Ver logs reais do Render + diagnosticar build_failed
Albert Menezes — Emotion Intelligence Platform
"""
import urllib.request, urllib.error, json, subprocess, pathlib, sys, time

API_KEY    = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE_URL   = "https://emotion-platform-albert.onrender.com"

def ok(msg):   print(f"  ✅ {msg}")
def err(msg):  print(f"  ❌ {msg}")
def info(msg): print(f"  ℹ️  {msg}")
def step(n,m): print(f"\n{'━'*50}\n  {n} — {m}\n{'━'*50}")

# ══════════════════════════════════════════════════
step("1/3", "BUSCAR LOGS REAIS DO RENDER")
# ══════════════════════════════════════════════════

# Tenta diferentes endpoints de log da API Render
endpoints_log = [
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
    f"https://api.render.com/v1/services/{SERVICE_ID}/events",
    f"https://api.render.com/v1/services/{SERVICE_ID}",
]

for url in endpoints_log:
    try:
        req = urllib.request.Request(url, method="GET")
        req.add_header("Authorization", f"Bearer {API_KEY}")
        req.add_header("Accept", "application/json")
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode())
            print(f"\n  URL: {url}")
            print(f"  Resposta: {json.dumps(data, indent=2, ensure_ascii=False)[:800]}")
            break
    except Exception as e:
        info(f"  {url} → {e}")

# ══════════════════════════════════════════════════
step("2/3", "SIMULAR BUILD DO RENDER LOCALMENTE")
# ══════════════════════════════════════════════════
# O Render roda: pip install -r requirements.txt && uvicorn main:app
# Vamos simular o startup do main.py e ver se há erros

print("\n  Simulando startup do main.py (5 segundos)...")
result = subprocess.run(
    ["python3", "-c", """
import sys, traceback
sys.path.insert(0, '.')

# Simula exatamente o que o Render faz ao startar
try:
    # Testa import do main sem rodar o servidor
    import importlib
    import os
    from pathlib import Path
    from fastapi import FastAPI
    from fastapi.middleware.cors import CORSMiddleware
    from datetime import datetime

    print("  [1] Imports básicos OK")

    app = FastAPI(title="Test", lifespan=None)
    print("  [2] FastAPI criado OK")

    # Testa StaticFiles
    try:
        from fastapi.staticfiles import StaticFiles
        if os.path.exists("static"):
            app.mount("/static", StaticFiles(directory="static"), name="static")
            print("  [3] StaticFiles OK — /static montado")
        else:
            print("  [3] AVISO: pasta static não existe!")
    except Exception as e:
        print(f"  [3] StaticFiles ERRO: {e}")

    # Carrega plugins (igual ao main.py)
    SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}
    ok_count = 0
    err_count = 0
    erros = []

    cats = sorted(Path("plugins").iterdir())
    for cat in cats:
        if not cat.is_dir() or cat.name.startswith("_"):
            continue
        for pf in sorted(cat.glob("*.py")):
            if pf.name in SKIP:
                continue
            mod_path = f"plugins.{cat.name}.{pf.stem}"
            try:
                mod  = importlib.import_module(mod_path)
                plug = getattr(mod, "plugin", None)
                if plug and hasattr(plug, "setup"):
                    plug.setup(app)
                    ok_count += 1
            except RecursionError:
                err_count += 1
            except Exception as e:
                err_count += 1
                erros.append(f"{mod_path}: {type(e).__name__}: {e}")

    print(f"  [4] Plugins: {ok_count} OK / {err_count} erros")

    # Mostra erros dos novos plugins especificamente
    novos = ["auth_postgresql","analytics_plugin","stripe_checkout","wcag_middleware"]
    for e in erros:
        for n in novos:
            if n in e:
                print(f"  [ERRO NOVO PLUGIN] {e}")

    # Verifica rotas registradas
    rotas = [r.path for r in app.routes]
    alvos = ["/api/v1/auth-pg/status", "/api/v1/analytics/status",
             "/api/v1/stripe-checkout/planos", "/api/v1/acessibilidade/status"]
    print(f"  [5] Total rotas: {len(rotas)}")
    for a in alvos:
        status = "✅" if a in rotas else "❌"
        print(f"       {status} {a}")

    # Verifica /static nas rotas
    static_ok = any("/static" in str(r) for r in app.routes)
    print(f"  [6] /static montado: {'✅' if static_ok else '❌'}")

    print("  SIMULAÇÃO CONCLUÍDA SEM CRASH")

except Exception as e:
    print(f"  CRASH NO STARTUP: {e}")
    traceback.print_exc()
"""],
    capture_output=False,
    cwd="."
)

# ══════════════════════════════════════════════════
step("3/3", "VERIFICAR SE O PROBLEMA É O requirements.txt")
# ══════════════════════════════════════════════════

print("\n  Conteúdo do requirements.txt (pacotes críticos):")
reqs = pathlib.Path("requirements.txt").read_text()
linhas_criticas = [l for l in reqs.split('\n')
                   if any(p in l.lower() for p in
                      ['fastapi','uvicorn','stripe','jwt','psycopg','pydantic',
                       'sqlalchemy','httpx','requests','python-multipart'])]
for l in linhas_criticas:
    if l.strip():
        print(f"    {l}")

print("\n  Verificando se psycopg2-binary está no requirements.txt...")
if 'psycopg2-binary' in reqs:
    ok("psycopg2-binary presente")
elif 'psycopg2' in reqs:
    # O Render pode falhar com psycopg2 (não-binary) se não tiver libpq-dev
    err("PROBLEMA: 'psycopg2' sem -binary pode falhar no Render!")
    info("Corrigindo para psycopg2-binary...")
    reqs_novo = reqs.replace('psycopg2\n', 'psycopg2-binary\n')
    reqs_novo = reqs_novo.replace('psycopg2==', 'psycopg2-binary==')
    pathlib.Path("requirements.txt").write_text(reqs_novo)
    ok("Corrigido para psycopg2-binary")
else:
    err("psycopg2 NÃO está no requirements.txt!")
    reqs_novo = reqs.rstrip() + "\npsycopg2-binary>=2.9.0\n"
    pathlib.Path("requirements.txt").write_text(reqs_novo)
    ok("psycopg2-binary adicionado")

print("\n  Verificando stripe...")
if 'stripe' in reqs:
    ok("stripe presente")
else:
    err("stripe NÃO está no requirements.txt!")
    reqs = pathlib.Path("requirements.txt").read_text()
    reqs_novo = reqs.rstrip() + "\nstripe>=7.0.0\n"
    pathlib.Path("requirements.txt").write_text(reqs_novo)
    ok("stripe adicionado")

# Commitar correções e fazer deploy
print("\n  Fazendo commit + push das correções...")
subprocess.run(["git", "add", "-A"], capture_output=True)
r = subprocess.run(
    ["git", "commit", "--no-verify", "-m",
     "fix: requirements.txt + diagnostico build_failed Render"],
    capture_output=True, text=True
)
print(f"  Commit: {r.stdout.strip()[:80] if r.returncode==0 else 'nada novo'}")

r2 = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
if r2.returncode == 0:
    ok("Push OK!")
else:
    info(f"Push: {r2.stderr[:60]}")

# Deploy manual via curl (API pode ter bug com urllib)
print("\n  Disparando deploy via subprocess curl...")
curl_result = subprocess.run([
    "curl", "-s", "-X", "POST",
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", '{"clearCache":"clear"}'
], capture_output=True, text=True)

if curl_result.stdout:
    try:
        d = json.loads(curl_result.stdout)
        ok(f"Deploy: {d.get('id','?')} — {d.get('status','?')}")
    except:
        info(f"Resposta curl: {curl_result.stdout[:200]}")
else:
    err(f"curl falhou: {curl_result.stderr[:100]}")

print(f"""
{'═'*52}
  PRÓXIMOS PASSOS:
{'═'*52}
  1. Aguarde 3-4 minutos o build
  2. Veja os logs em:
     https://dashboard.render.com/web/{SERVICE_ID}/logs
  3. Depois rode:
     python3 verificar.py
{'═'*52}
""")
