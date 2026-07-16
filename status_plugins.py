#!/usr/bin/env python3
"""
Status de todos os plugins instalados
Uso: python3 status_plugins.py
"""
import py_compile
from pathlib import Path
from datetime import datetime

PLUGINS_DIR = Path("plugins")
CATEGORIAS = [
    "seguranca","sistemas","ia","saude","social",
    "analytics","performance","monetizacao","integracao","frontend"
]

print(f"\n{'═'*55}")
print(f"  EMOTION PLATFORM — STATUS DOS PLUGINS")
print(f"  {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print(f"{'═'*55}")

total = 0
ok = 0
erros = []

for categoria in CATEGORIAS:
    pasta = PLUGINS_DIR / categoria
    if not pasta.exists():
        continue

    plugins = [f for f in pasta.glob("*.py") if not f.name.startswith("_")]
    if not plugins:
        continue

    print(f"\n  📦 {categoria.upper()} ({len(plugins)} plugins)")

    for plugin in sorted(plugins):
        total += 1
        try:
            py_compile.compile(str(plugin), doraise=True)
            linhas = len(plugin.read_text().split("\n"))
            print(f"    ✅ {plugin.stem:<30} ({linhas:,} linhas)")
            ok += 1
        except py_compile.PyCompileError as e:
            print(f"    ❌ {plugin.stem:<30} ERRO: {str(e)[:40]}")
            erros.append(plugin.stem)

print(f"\n{'─'*55}")
print(f"  Total:  {total} plugins")
print(f"  OK:     {ok}")
print(f"  Erros:  {len(erros)}")
print(f"  Score:  {round(ok/total*100) if total > 0 else 0}%")
print(f"{'═'*55}\n")
