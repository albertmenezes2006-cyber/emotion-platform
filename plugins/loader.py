"""Loader Universal — registra APIRouters sem sub-apps (evita RecursionError)"""
import os, importlib, logging
from pathlib import Path

logger = logging.getLogger(__name__)
SKIP = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}

def load_all_plugins(app):
    base = Path(__file__).parent
    ok = err = 0
    for cat in sorted(base.iterdir()):
        if not cat.is_dir() or cat.name.startswith("_"): continue
        for pf in sorted(cat.glob("*.py")):
            if pf.name in SKIP: continue
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
    logger.info(f"Plugins: {ok} OK / {err} ignorados | Rotas: {len(app.routes)}")
    return ok, err
