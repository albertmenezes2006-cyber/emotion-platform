"""
Debug: descobrir por que os plugins não carregam no Render
Albert Menezes — Emotion Intelligence Platform
"""
import pathlib, subprocess, json, urllib.request

def ok(msg):   print(f"  ✅ {msg}")
def err(msg):  print(f"  ❌ {msg}")
def info(msg): print(f"  ℹ️  {msg}")

# ══════════════════════════════════════
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  1 — VER LOGS DO RENDER (último deploy)")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

API_KEY    = "rnd_MgylgwI58qn8mY5ReSDpa8hfCFQK"
SERVICE_ID = "srv-d97vrmcs728c73ci1mig"

# Pegar último deploy ID
try:
    req = urllib.request.Request(
        f"https://api.render.com/v1/services/{SERVICE_ID}/deploys?limit=1",
        method="GET"
    )
    req.add_header("Authorization", f"Bearer {API_KEY}")
    req.add_header("Accept", "application/json")
    with urllib.request.urlopen(req, timeout=15) as r:
        deploys = json.loads(r.read().decode())
        if deploys:
            d = deploys[0].get("deploy", deploys[0])
            deploy_id = d.get("id", "?")
            status    = d.get("status", "?")
            ok(f"Último deploy: {deploy_id} — status: {status}")
        else:
            info("Nenhum deploy encontrado")
except Exception as e:
    err(f"API Render: {e}")

# ══════════════════════════════════════
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  2 — TESTAR PLUGIN LOCALMENTE (simular o Render)")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

import sys
sys.path.insert(0, ".")

# Simular exatamente o que o main.py faz
import importlib
from pathlib import Path

SKIP = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}

plugins_encontrados = {}
plugins_com_setup   = []
plugins_sem_setup   = []
plugins_com_erro    = []

base = Path("plugins")
for cat in sorted(base.iterdir()):
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
                plugins_com_setup.append(mod_path)
            else:
                plugins_sem_setup.append(mod_path)
                plugins_encontrados[mod_path] = "sem plugin.setup()"
        except Exception as e:
            plugins_com_erro.append((mod_path, str(e)))

ok(f"Com plugin.setup(): {len(plugins_com_setup)}")
info(f"Sem plugin.setup(): {len(plugins_sem_setup)}")
info(f"Com erro de import: {len(plugins_com_erro)}")

# Verificar especificamente os 4 novos
print("\n  Verificando os 4 plugins novos:")
alvos = [
    "plugins.auth_real.auth_postgresql",
    "plugins.analytics.analytics_plugin",
    "plugins.monetizacao_real.stripe_checkout",
    "plugins.acessibilidade.wcag_middleware",
]
for p in alvos:
    if p in plugins_com_setup:
        ok(f"{p.split('.')[-1]}")
    elif p in plugins_sem_setup:
        err(f"{p.split('.')[-1]} → importou mas SEM plugin.setup()")
    else:
        # Verificar se deu erro
        erros_p = [e for m, e in plugins_com_erro if m == p]
        if erros_p:
            err(f"{p.split('.')[-1]} → ERRO: {erros_p[0]}")
        else:
            err(f"{p.split('.')[-1]} → NÃO ENCONTRADO")

# ══════════════════════════════════════
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  3 — VERIFICAR __init__.py DOS DIRETÓRIOS")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

dirs_checar = [
    "plugins/analytics",
    "plugins/acessibilidade",
    "plugins/auth_real",
    "plugins/monetizacao_real",
]
for d in dirs_checar:
    init = pathlib.Path(d) / "__init__.py"
    py_files = list(pathlib.Path(d).glob("*.py")) if pathlib.Path(d).exists() else []
    print(f"\n  📁 {d}/")
    print(f"     __init__.py: {'✅ existe' if init.exists() else '❌ FALTA'}")
    for f in py_files:
        tamanho = f.stat().st_size
        print(f"     📄 {f.name} ({tamanho} bytes)")

# ══════════════════════════════════════
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  4 — VER CONTEÚDO DO analytics_plugin.py (primeiras 10 linhas)")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

for arq in ["plugins/analytics/analytics_plugin.py",
            "plugins/acessibilidade/wcag_middleware.py",
            "plugins/auth_real/auth_postgresql.py",
            "plugins/monetizacao_real/stripe_checkout.py"]:
    p = pathlib.Path(arq)
    if p.exists():
        lines = p.read_text().split('\n')
        print(f"\n  === {arq} (últimas 5 linhas) ===")
        for l in lines[-6:]:
            print(f"    {l}")
    else:
        err(f"{arq} NÃO EXISTE!")

# ══════════════════════════════════════
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  5 — VER STATIC NO main.py")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

main_txt = pathlib.Path("main.py").read_text()
for i, linha in enumerate(main_txt.split('\n'), 1):
    if 'static' in linha.lower() or 'StaticFiles' in linha:
        print(f"  linha {i:3}: {linha}")

# ══════════════════════════════════════
print("\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print("  6 — GIT STATUS (o que está no GitHub)")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

r = subprocess.run(["git", "log", "--oneline", "-5"], capture_output=True, text=True)
print(r.stdout)

r2 = subprocess.run(["git", "show", "--stat", "HEAD"], capture_output=True, text=True)
print(r2.stdout[:800])

