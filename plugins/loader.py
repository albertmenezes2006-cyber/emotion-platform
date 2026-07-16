"""
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
