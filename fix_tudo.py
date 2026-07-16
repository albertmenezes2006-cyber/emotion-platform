#!/usr/bin/env python3
"""Corrige loader.py + status_plugins.py para detectar TODOS os plugins"""
import os

def w(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)
    print(f"✅ {path}")

# ══════════════════════════════════════════════
# 1. REESCREVER loader.py — detecta TUDO automaticamente
# ══════════════════════════════════════════════
w("plugins/loader.py", '''"""
Loader Universal — detecta e carrega TODOS os plugins automaticamente
"""
import os, importlib, logging, traceback
from pathlib import Path

logger = logging.getLogger(__name__)

def load_all_plugins(app):
    plugins_dir = Path(__file__).parent
    total_ok = 0
    total_err = 0
    erros = []

    for cat_dir in sorted(plugins_dir.iterdir()):
        if not cat_dir.is_dir(): continue
        if cat_dir.name.startswith("_"): continue

        for plugin_file in sorted(cat_dir.glob("*.py")):
            if plugin_file.name.startswith("_"): continue
            if plugin_file.name in ("loader.py", "plugin_base.py"): continue

            module_path = f"plugins.{cat_dir.name}.{plugin_file.stem}"
            try:
                mod = importlib.import_module(module_path)
                if hasattr(mod, "plugin"):
                    mod.plugin.setup(app)
                    total_ok += 1
                    logger.debug(f"[OK] {module_path}")
            except Exception as e:
                total_err += 1
                erros.append(f"{module_path}: {e}")
                logger.warning(f"[ERRO] {module_path}: {e}")

    logger.info(f"Plugins carregados: {total_ok} OK, {total_err} erros")
    if erros:
        for e in erros:
            logger.warning(f"  ↳ {e}")
    return total_ok, total_err
''')

# ══════════════════════════════════════════════
# 2. REESCREVER status_plugins.py — conta TUDO
# ══════════════════════════════════════════════
w("status_plugins.py", '''#!/usr/bin/env python3
"""Status UNIVERSAL — conta todos os plugins de todas as categorias"""
import os, sys
from datetime import datetime

G="\033[92m"; R="\033[91m"; C="\033[96m"; B="\033[1m"; X="\033[0m"; Y="\033[93m"

def ok(path):
    try:
        import py_compile
        py_compile.compile(path, doraise=True)
        return True
    except:
        return False

def linhas(path):
    try:
        return len(open(path).readlines())
    except:
        return 0

cats = {}
skip = {"__pycache__","__init__.py","loader.py","plugin_base.py"}
pdir = "plugins"

for cat in sorted(os.listdir(pdir)):
    cpath = os.path.join(pdir, cat)
    if not os.path.isdir(cpath) or cat.startswith("_"): continue
    plugins = []
    for f in sorted(os.listdir(cpath)):
        if not f.endswith(".py") or f in skip: continue
        fp = os.path.join(cpath, f)
        plugins.append({"n": f[:-3], "ok": ok(fp), "l": linhas(fp)})
    if plugins:
        cats[cat] = plugins

total = sum(len(v) for v in cats.values())
oks   = sum(sum(1 for p in v if p["ok"]) for v in cats.values())
errs  = total - oks
score = round(oks/total*100,1) if total else 0

print()
print(f"{B}{'═'*62}{X}")
print(f"{B}  EMOTION PLATFORM — STATUS COMPLETO v2.0{X}")
print(f"  {datetime.now().strftime('%d/%m/%Y %H:%M')} | Meta: 1470 plugins")
print(f"{B}{'═'*62}{X}")
print()

for cat, plugins in cats.items():
    n_ok = sum(1 for p in plugins if p["ok"])
    cor = G if n_ok==len(plugins) else Y if n_ok>0 else R
    print(f"  {C}📦 {cat.upper()} ({len(plugins)} plugins){X}")
    for pl in plugins:
        ic = f"{G}✅{X}" if pl["ok"] else f"{R}❌{X}"
        print(f"    {ic} {pl['n']:<42} ({pl['l']} linhas)")
    print()

print(f"{'─'*62}")
print(f"  {B}Total plugins:{X}  {total}")
print(f"  {G}OK:{X}            {oks}")
print(f"  {R}Erros:{X}         {errs}")
sc = G if score>=95 else Y if score>=80 else R
print(f"  {B}Score:{X}         {sc}{score}%{X}")
print(f"  {B}Progresso:{X}     {total}/1470 = {round(total/1470*100,1)}%")
print(f"{'═'*62}")
''')

# ══════════════════════════════════════════════
# 3. GARANTIR __init__.py em TODAS as pastas
# ══════════════════════════════════════════════
for cat in os.listdir("plugins"):
    cpath = os.path.join("plugins", cat)
    if os.path.isdir(cpath) and not cat.startswith("_"):
        init = os.path.join(cpath, "__init__.py")
        if not os.path.exists(init):
            open(init, "w").close()
            print(f"✅ __init__.py criado em {cpath}")

# ══════════════════════════════════════════════
# 4. CONTAR TODOS OS PLUGINS EXISTENTES
# ══════════════════════════════════════════════
skip = {"__init__.py","loader.py","plugin_base.py"}
total = 0
cats_count = {}
for cat in os.listdir("plugins"):
    cpath = os.path.join("plugins", cat)
    if not os.path.isdir(cpath) or cat.startswith("_"): continue
    for f in os.listdir(cpath):
        if f.endswith(".py") and f not in skip:
            total += 1
            cats_count[cat] = cats_count.get(cat, 0) + 1

print(f"\n{'='*62}")
print(f"TOTAL DE PLUGINS NO DISCO: {total}")
print(f"PROGRESSO: {total}/1470 = {round(total/1470*100,1)}%")
print(f"{'='*62}")
print(f"\n{'CATEGORIA':<35} {'QTD':>5}")
print("-"*42)
for cat, n in sorted(cats_count.items(), key=lambda x: -x[1]):
    print(f"  {cat:<33} {n:>5}")
print("-"*42)
print(f"  {'TOTAL':<33} {total:>5}")
