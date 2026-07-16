#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.3"""
import os, sys, logging
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# Aumentar limite de recursao para Python 3.14
sys.setrecursionlimit(10000)

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("ep")

app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1481 plugins de saude mental",
    version="24.3.0",
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
    return {"status":"ok","version":"24.3.0","plugins":_ok,
            "erros":_err,"rotas":len(app.routes),
            "uptime":str(datetime.utcnow()-_start)}

@app.get("/ping")
async def ping():
    return {"pong":True,"ts":datetime.utcnow().isoformat()}

# Carregar plugins em lotes pequenos para evitar stack overflow
SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}

log.info("Carregando plugins em lotes...")
import importlib

cats = sorted(Path("plugins").iterdir())
for cat in cats:
    if not cat.is_dir() or cat.name.startswith("_"):
        continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP:
            continue
        mod_path = f"plugins.{cat.name}.{pf.stem}"
        try:
            mod = importlib.import_module(mod_path)
            plug = getattr(mod, "plugin", None)
            if plug and hasattr(plug, "setup"):
                plug.setup(app)
                _ok += 1
        except RecursionError:
            _err += 1
            log.warning(f"RecursionError em {mod_path} — pulando")
        except Exception as e:
            _err += 1
            log.debug(f"skip {mod_path}: {type(e).__name__}")

log.info(f"Plugins: {_ok} OK / {_err} err | Rotas: {len(app.routes)}")
