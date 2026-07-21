#!/usr/bin/env python3
"""Status UNIVERSAL — detecta TODOS os plugins automaticamente"""
import os
import py_compile
from datetime import datetime

G="[92m"; R="[91m"; C="[96m"; B="[1m"; X="[0m"; Y="[93m"; M="[95m"

SKIP = {"__init__.py","loader.py","plugin_base.py"}

def chk(path):
    try: py_compile.compile(path, doraise=True); return True
    except: return False

def lns(path):
    try: return len(open(path).readlines())
    except: return 0

cats = {}
for cat in sorted(os.listdir("plugins")):
    cp = os.path.join("plugins", cat)
    if not os.path.isdir(cp) or cat.startswith("_"): continue
    pls = []
    for f in sorted(os.listdir(cp)):
        if not f.endswith(".py") or f in SKIP: continue
        fp = os.path.join(cp, f)
        pls.append({"n": f[:-3], "ok": chk(fp), "l": lns(fp)})
    if pls:
        cats[cat] = pls

total = sum(len(v) for v in cats.values())
oks   = sum(sum(1 for p in v if p["ok"]) for v in cats.values())
errs  = total - oks
score = round(oks/total*100,1) if total else 0

print()
print(f"{B}{"="*65}{X}")
print(f"{B}  🧠 EMOTION INTELLIGENCE PLATFORM — STATUS COMPLETO{X}")
print(f"  {datetime.now().strftime("%d/%m/%Y %H:%M")} | Meta: 1.470 plugins")
print(f"{B}{"="*65}{X}")
print()

for cat, pls in cats.items():
    n_ok = sum(1 for p in pls if p["ok"])
    cor = G if n_ok==len(pls) else Y
    print(f"  {C}📦 {cat.upper():<30} ({len(pls):>3} plugins){X}")
    for pl in pls:
        ic = f"{G}✅{X}" if pl["ok"] else f"{R}❌{X}"
        print(f"    {ic} {pl["n"]:<45} ({pl["l"]:>4} linhas)")
    print()

print(f"{"─"*65}")
print(f"  {B}Total plugins:{X}    {M}{total}{X}")
print(f"  {G}OK:{X}              {oks}")
print(f"  {R}Erros:{X}           {errs}")
sc = G if score>=95 else Y if score>=80 else R
print(f"  {B}Score:{X}           {sc}{score}%{X}")
print(f"  {B}Progresso:{X}       {M}{total}/1470 = {round(total/1470*100,1)}%{X}")
pct = total/1470*100
bar = int(pct/2)
print(f"  [{"█"*bar}{"░"*(50-bar)}] {round(pct,1)}%")
print(f"{"="*65}")
