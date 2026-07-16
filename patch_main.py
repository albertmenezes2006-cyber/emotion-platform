#!/usr/bin/env python3
"""
Patch seguro para main.py — roda ANTES do uvicorn
Monta static files e carrega plugins sem modificar main.py
"""
import os, sys, logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importar app do main
sys.path.insert(0, ".")
from main import app

# Montar static files
try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
        logger.info("✅ Static files montados")
except Exception as e:
    logger.warning(f"Static: {e}")

# Carregar todos os plugins
try:
    from plugins.loader import load_all_plugins
    ok, err = load_all_plugins(app)
    logger.info(f"✅ Plugins: {ok} carregados, {err} ignorados")
    logger.info(f"✅ Rotas totais: {len(app.routes)}")
except Exception as e:
    logger.error(f"Loader error: {e}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
