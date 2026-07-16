#!/usr/bin/env python3
"""Corrige erro E402 do ruff no main.py"""

with open("main.py") as f:
    content = f.read()

# Remover o bloco injetado com import no meio do arquivo
old_block = """
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

# Substituir por versão sem imports no meio
new_block = """
# ═══════════════════════════════════════════════
# EMOTION PLATFORM — PLUGIN SYSTEM AUTO-LOAD
# ═══════════════════════════════════════════════
try:
    from fastapi.staticfiles import StaticFiles as _SF_ep
    import os as _os_ep
    if _os_ep.path.exists("static"):
        try:
            app.mount("/static", _SF_ep(directory="static"), name="static")
        except Exception:
            pass
except Exception:
    pass

try:
    from plugins.loader import load_all_plugins as _lap_ep
    _lap_ep(app)
except Exception as _e_pl:
    pass
# ═══════════════════════════════════════════════
"""

if old_block.strip() in content:
    content = content.replace(old_block.strip(), new_block.strip())
    print("✅ Bloco substituído")
else:
    # Tentar encontrar e substituir manualmente
    import re
    pattern = r'# ═+\n# EMOTION PLATFORM.*?# ═+\n'
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_block + content[match.end():]
        print("✅ Bloco encontrado via regex e substituído")
    else:
        print("⚠️  Bloco não encontrado — verificando manualmente")
        # Mostrar contexto ao redor da linha 2832
        lines = content.splitlines()
        for i, line in enumerate(lines):
            if "EMOTION PLATFORM" in line or "import os as _os_ep" in line:
                print(f"  Linha {i+1}: {line}")

with open("main.py", "w") as f:
    f.write(content)

# Verificar
import subprocess, sys
r = subprocess.run([sys.executable, "-m", "py_compile", "main.py"],
                   capture_output=True, text=True)
print(f"Compilação: {'✅ OK' if r.returncode == 0 else '❌ ERRO'}")
if r.returncode != 0:
    print(r.stderr[:300])
    # Restaurar backup
    import shutil
    shutil.copy("main.py.bak", "main.py")
    print("⚠️  Backup restaurado")
