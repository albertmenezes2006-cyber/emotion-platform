#!/usr/bin/env python3
import subprocess
import time
import json
import os
from datetime import datetime

BASE = "https://emotion-platform-albert.onrender.com"
RESULTADOS = {}


def rodar(nome, cmd, timeout=120):
    print(f"\n=======================================================")
    print(f"  {nome}")
    print(f"=======================================================")
    inicio = time.time()
    r = subprocess.run(cmd, shell=True, timeout=timeout)
    tempo = round(time.time() - inicio, 1)
    ok = r.returncode == 0
    RESULTADOS[nome] = {"ok": ok, "tempo": tempo}
    return ok


print("=" * 60)
print("  ANALISE COMPLETA — EmotionAI")
print(f"  {datetime.now().strftime('%d/%m/%Y %H:%M')}")
print("=" * 60)

rodar("1. Compilacao",     "python3 -m py_compile main.py && echo OK")
rodar("2. Plugins",        "python3 status_plugins.py 2>/dev/null | grep -E 'Total|Score'")
rodar("3. Testes API",     "pytest tests/test_api.py -v --tb=short 2>&1 | tail -20")
rodar("4. Seguranca",      "python3 tools/security.py")
rodar("5. Performance",    "python3 tools/performance.py")
rodar("6. Acessibilidade", "python3 tools/accessibility.py")
rodar("7. SSL",            "python3 tools/ssl_check.py")
rodar("8. SEO",            "python3 tools/seo_check.py")
rodar("9. Browser Real",   "python3 tests/test_browser.py", timeout=300)

print("\n" + "=" * 60)
print("  RELATORIO FINAL")
print("=" * 60)

ok_n = sum(1 for v in RESULTADOS.values() if v["ok"])
total = len(RESULTADOS)
score = round(ok_n / total * 100) if total > 0 else 0

print(f"\n  Score: {ok_n}/{total} ({score}%)")
print()
for nome, r in RESULTADOS.items():
    icon = "OK" if r["ok"] else "XX"
    print(f"  [{icon}] {nome} ({r['tempo']}s)")

shots_dir = "tests/screenshots"
if os.path.exists(shots_dir):
    shots = os.listdir(shots_dir)
    if shots:
        print(f"\n  Screenshots ({len(shots)}):")
        for s in sorted(shots):
            print(f"    • {s}")

ts = datetime.now().strftime("%Y%m%d_%H%M")
with open(f"tests/relatorio_{ts}.json", "w", encoding="utf-8") as f:
    json.dump(
        {"data": str(datetime.now()), "score": f"{ok_n}/{total}", "resultados": RESULTADOS},
        f, indent=2, ensure_ascii=False
    )

print(f"\n  Relatorio: tests/relatorio_{ts}.json")
print(f"  Site: {BASE}")
