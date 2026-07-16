"""Loader Universal — tolerante a todos os erros"""
import os, importlib, logging
from pathlib import Path

logger = logging.getLogger(__name__)

SKIP_FILES = {"__init__.py", "loader.py", "plugin_base.py"}
SKIP_DIRS  = {"__pycache__"}

def load_all_plugins(app):
    base = Path(__file__).parent
    ok = err = 0

    for cat in sorted(base.iterdir()):
        if not cat.is_dir() or cat.name in SKIP_DIRS or cat.name.startswith("_"):
            continue
        for pf in sorted(cat.glob("*.py")):
            if pf.name in SKIP_FILES or pf.name.startswith("_"):
                continue
            mod_path = f"plugins.{cat.name}.{pf.stem}"
            try:
                mod = importlib.import_module(mod_path)
                plug = getattr(mod, "plugin", None)
                if plug and hasattr(plug, "setup"):
                    plug.setup(app)
                    ok += 1
                else:
                    err += 1
            except Exception as e:
                err += 1
                logger.debug(f"skip {mod_path}: {e}")

    logger.info(f"Plugins: {ok} OK / {err} ignorados")
    return ok, err
