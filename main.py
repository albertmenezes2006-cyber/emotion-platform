#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.0"""
import os, logging, importlib
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("ep")

# App sem lifespan para evitar RecursionError com 1477 plugins
app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1477 plugins de saude mental com IA",
    version="24.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=None
)

app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass

_start = datetime.utcnow()
_ok = 0
_err = 0

@app.get("/health")
async def health():
    return {"status":"ok","version":"24.0.0",
            "plugins":_ok,"rotas":len(app.routes),
            "uptime":str(datetime.utcnow()-_start)}

@app.get("/ping")
async def ping():
    return {"pong":True,"ts":datetime.utcnow().isoformat()}

# Carregar plugins inline sem sub-apps
SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}
for cat in sorted(Path("plugins").iterdir()):
    if not cat.is_dir() or cat.name.startswith("_"): continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP: continue
        try:
            mod = importlib.import_module(f"plugins.{cat.name}.{pf.stem}")
            plug = getattr(mod, "plugin", None)
            if plug and hasattr(plug, "setup"):
                plug.setup(app)
                _ok += 1
        except Exception as e:
            _err += 1
            log.debug(f"skip: {e}")

log.info(f"Plugins: {_ok} OK | Rotas: {len(app.routes)}")
