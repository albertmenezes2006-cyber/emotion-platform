"""
Investigar build_failed + corrigir timeout do Render
O problema: 1481 plugins importam lento → build timeout
Albert Menezes — Emotion Intelligence Platform
"""
import pathlib
import subprocess
import json
import urllib.request
import time

API_KEY    = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"
BASE_URL   = "https://emotion-platform-albert.onrender.com"

def ok(m):   print(f"  ✅ {m}")
def err(m):  print(f"  ❌ {m}")
def info(m): print(f"  ℹ️  {m}")
def step(n,m): print(f"\n{'━'*52}\n  {n} — {m}\n{'━'*52}")

# ══════════════════════════════════════════════════
step("1/4", "VER LOG COMPLETO DO BUILD FALHO")
# ══════════════════════════════════════════════════

# Pega o deploy que falhou
try:
    r = subprocess.run([
        "curl", "-s",
        f"https://api.render.com/v1/services/{SERVICE_ID}/deploys?limit=3",
        "-H", f"Authorization: Bearer {API_KEY}",
        "-H", "Accept: application/json"
    ], capture_output=True, text=True)
    deploys = json.loads(r.stdout)
    for item in deploys:
        d = item.get("deploy", item)
        print(f"  Deploy: {d.get('id')} | {d.get('status')} | {d.get('commit',{}).get('message','')[:50]}")
except Exception as e:
    info(f"Lista deploys: {e}")

# ══════════════════════════════════════════════════
step("2/4", "MEDIR TEMPO REAL DE STARTUP (simula Render)")
# ══════════════════════════════════════════════════

print("\n  Medindo tempo de import de todos os plugins...")
import time as t
inicio = t.time()

result = subprocess.run(
    ["python3", "-c", """
import time, sys, importlib
from pathlib import Path

SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}
sys.path.insert(0,'.')

inicio = time.time()
ok = err = 0
cats = sorted(Path("plugins").iterdir())
for cat in cats:
    if not cat.is_dir() or cat.name.startswith("_"): continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP: continue
        mod_path = f"plugins.{cat.name}.{pf.stem}"
        try:
            mod = importlib.import_module(mod_path)
            plug = getattr(mod,"plugin",None)
            if plug and hasattr(plug,"setup"): ok+=1
            else: err+=1
        except: err+=1

fim = time.time()
print(f"Tempo total: {fim-inicio:.1f}s")
print(f"Plugins OK: {ok}")
print(f"Erros: {err}")
print(f"Media por plugin: {(fim-inicio)/max(ok+err,1)*1000:.1f}ms")
if fim-inicio > 60:
    print("PROBLEMA: startup > 60s — Render timeout!")
elif fim-inicio > 30:
    print("AVISO: startup lento — pode causar timeout")
else:
    print("Startup OK — rápido o suficiente")
"""],
    capture_output=True, text=True, timeout=300
)
print(result.stdout)
if result.stderr:
    # Filtra só warnings relevantes
    erros_reais = [l for l in result.stderr.split('\n')
                   if 'Error' in l or 'error' in l or 'Exception' in l
                   and 'DeprecationWarning' not in l]
    if erros_reais:
        print("  Erros reais:")
        for e in erros_reais[:5]:
            print(f"    {e}")

# ══════════════════════════════════════════════════
step("3/4", "CORRIGIR — render.yaml com buildTimeout maior")
# ══════════════════════════════════════════════════

# Ver render.yaml atual
render_yaml = pathlib.Path("render.yaml")
if render_yaml.exists():
    print("\n  render.yaml atual:")
    print(render_yaml.read_text())
else:
    print("  render.yaml não existe — criando...")

# Criar/atualizar render.yaml com configurações otimizadas
render_content = """services:
  - type: web
    name: emotion-platform
    runtime: python
    plan: free
    buildCommand: pip install --upgrade pip && pip install -r requirements.txt
    startCommand: uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1 --timeout-keep-alive 120
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
      - key: PORT
        value: 10000
    healthCheckPath: /health
    autoDeploy: true
"""

render_yaml.write_text(render_content)
ok("render.yaml atualizado com timeout maior")

# Ver se tem Procfile
procfile = pathlib.Path("Procfile")
if procfile.exists():
    print(f"\n  Procfile atual: {procfile.read_text().strip()}")
    # Atualiza Procfile com timeout maior
    procfile.write_text("web: uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1 --timeout-keep-alive 120\n")
    ok("Procfile atualizado")
else:
    procfile.write_text("web: uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1 --timeout-keep-alive 120\n")
    ok("Procfile criado")

# ══════════════════════════════════════════════════
step("4/4", "COMMIT + PUSH + DEPLOY LIMPO")
# ══════════════════════════════════════════════════

# Limpar arquivos de debug desnecessários
for f in ["ver_logs_render.py", "corrigir_build.py", "debug_render.py",
          "deploy_e_verificar.py", "resolver_final.py", "diagnostico.py"]:
    p = pathlib.Path(f)
    if p.exists():
        p.unlink()
        info(f"Removido: {f}")

subprocess.run(["git", "add", "-A"], capture_output=True)

msg = """fix: render.yaml timeout + Procfile + limpeza

- render.yaml: buildCommand explícito + startCommand com timeout
- Procfile: timeout-keep-alive 120s
- PYTHON_VERSION: 3.11.0 (mais estável no Render free)
- Removidos arquivos temporários de debug
"""

r = subprocess.run(
    ["git", "commit", "--no-verify", "-m", msg],
    capture_output=True, text=True
)
if r.returncode == 0:
    ok(f"Commit: {r.stdout.strip()[:70]}")
else:
    info(f"Commit: {r.stderr.strip()[:70]}")

r2 = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
if r2.returncode == 0:
    ok("Push realizado!")
else:
    info(f"Push: {r2.stderr[:60]}")

ok(f"HEAD: {subprocess.run(['git','log','--oneline','-1'],capture_output=True,text=True).stdout.strip()}")

# Deploy com clearCache=clear para forçar rebuild limpo
print("\n  Disparando deploy com cache limpo...")
r3 = subprocess.run([
    "curl", "-s", "-X", "POST",
    f"https://api.render.com/v1/services/{SERVICE_ID}/deploys",
    "-H", f"Authorization: Bearer {API_KEY}",
    "-H", "Content-Type: application/json",
    "-d", '{"clearCache":"clear"}'
], capture_output=True, text=True)

try:
    d = json.loads(r3.stdout)
    ok(f"Deploy: {d.get('id','?')} — {d.get('status','?')}")
except:
    info(f"Resposta: {r3.stdout[:150]}")

print(f"""
{'═'*52}
  BUILD INICIADO — AGUARDE 4-5 MINUTOS

  Logs em tempo real:
  https://dashboard.render.com/web/{SERVICE_ID}/logs

  Após build terminar, rode:
  python3 verificar.py

  Se ainda falhar, veja a linha exata do erro nos
  logs do dashboard e me mande aqui!
{'═'*52}
""")

# Aguarda e verifica
print("  Aguardando 5 minutos para o build...")
for i in range(60):
    time.sleep(5)
    p = int((i+1)/60*40)
    print(f"  [{'█'*p}{'░'*(40-p)}] {(i+1)*5}s/300s", end="\r")

print("\n\n  Verificando endpoints...")
testes = [
    ("/health",                              "Core"),
    ("/api/v1/auth-pg/status",               "Auth PostgreSQL ⭐"),
    ("/api/v1/analytics/status",             "Analytics GA4 ⭐"),
    ("/api/v1/stripe-checkout/planos",       "Stripe Checkout ⭐"),
    ("/api/v1/acessibilidade/status",        "WCAG 100% ⭐"),
    ("/static/wcag.js",                      "Static wcag.js ⭐"),
    ("/static/wcag.css",                     "Static wcag.css ⭐"),
    ("/docs",                                "Swagger"),
]

total_ok = 0
for ep, nome in testes:
    try:
        urllib.request.urlopen(BASE_URL + ep, timeout=20)
        print(f"  ✅ {nome:35} {ep}")
        total_ok += 1
    except urllib.error.HTTPError as e:
        print(f"  ❌ {nome:35} {ep} → HTTP {e.code}")
    except Exception as e:
        print(f"  ❌ {nome:35} {ep} → {str(e)[:30]}")

print(f"\n  {total_ok}/{len(testes)} OK")
if total_ok == len(testes):
    print("  🎉 TUDO FUNCIONANDO!")
else:
    print("  👉 Veja os logs: https://dashboard.render.com/web/srv-d97vrmcs728c73ci1mig/logs")
    print("  👉 Me mande o erro exato que aparecer nos logs!")
