#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.0 — Entry Point"""
import os
import logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("emotion_platform")

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1477 plugins de saude mental com IA",
    version="24.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])

# Static files
try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
        logger.info("Static OK")
except Exception as e:
    logger.warning(f"Static: {e}")

# Health check ANTES dos plugins (sempre responde)
_start_time = __import__("datetime").datetime.utcnow()

@app.get("/health")
async def health():
    uptime = str(__import__("datetime").datetime.utcnow() - _start_time)
    return {"status": "ok", "version": "24.0.0", "uptime": uptime,
            "plugins": _plugins_ok, "rotas": len(app.routes)}

@app.get("/")
async def root():
    return JSONResponse({"platform": "Emotion Intelligence Platform v24.0",
                         "docs": "/docs", "health": "/health",
                         "avaliacao": "/app/avaliacao", "chat": "/app/chat"})

# Carregar plugins com log detalhado
_plugins_ok = 0
_plugins_err = 0

try:
    logger.info("Carregando plugins...")
    import importlib
    from pathlib import Path

    SKIP = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}
    plugins_dir = Path("plugins")

    for cat_dir in sorted(plugins_dir.iterdir()):
        if not cat_dir.is_dir() or cat_dir.name.startswith("_"): continue
        for pf in sorted(cat_dir.glob("*.py")):
            if pf.name in SKIP: continue
            mod_path = f"plugins.{cat_dir.name}.{pf.stem}"
            try:
                mod = importlib.import_module(mod_path)
                plug = getattr(mod, "plugin", None)
                if plug and hasattr(plug, "setup"):
                    plug.setup(app)
                    _plugins_ok += 1
            except Exception as e:
                _plugins_err += 1
                logger.debug(f"skip {mod_path}: {e}")

    logger.info(f"Plugins: {_plugins_ok} OK / {_plugins_err} ignorados")
    logger.info(f"Rotas totais: {len(app.routes)}")

except Exception as e:
    logger.error(f"Erro critico ao carregar plugins: {e}")
    import traceback
    logger.error(traceback.format_exc())
