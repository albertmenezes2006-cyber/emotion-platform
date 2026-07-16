"""
Loader Universal — monta plugins como sub-aplicação em /ep/
Evita conflito com rotas do main.py original
"""
import os, importlib, logging
from pathlib import Path
from fastapi import FastAPI

logger = logging.getLogger(__name__)

SKIP_FILES = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}
SKIP_DIRS  = {"__pycache__"}

def load_all_plugins(app):
    """
    Carrega plugins direto no app principal.
    Rotas dos plugins usam /api/v1/ mas só se não conflitarem.
    """
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


def create_plugin_app():
    """
    Cria uma FastAPI separada só com os plugins.
    Monte em /ep/ no app principal para evitar conflitos.
    Uso: app.mount("/ep", create_plugin_app())
    """
    plugin_app = FastAPI(
        title="Emotion Platform — Plugin APIs",
        description="1477 plugins de saúde mental",
        version="23.0.0",
        docs_url="/docs",
        redoc_url="/redoc"
    )

    # Montar static se existir
    try:
        from fastapi.staticfiles import StaticFiles
        if os.path.exists("static"):
            plugin_app.mount("/static", StaticFiles(directory="static"), name="static_ep")
    except Exception:
        pass

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
                    plug.setup(plugin_app)
                    ok += 1
                else:
                    err += 1
            except Exception as e:
                err += 1
                logger.debug(f"skip {mod_path}: {e}")

    logger.info(f"Plugin app: {ok} plugins, {err} ignorados")

    @plugin_app.get("/health")
    async def health():
        return {"status": "ok", "plugins": ok, "version": "23.0.0"}

    return plugin_app
