#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.2 — load antes do app"""
import os, logging, importlib, sys
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

logging.basicConfig(level=logging.INFO,
    format="%(asctime)s %(levelname)s: %(message)s")
log = logging.getLogger("ep")

SKIP = {"__init__.py","loader.py","plugin_base.py","db_manager.py"}
_ok = 0
_err = 0
_routers = []

# Passo 1: importar todos os modulos e coletar routers
log.info("Importando plugins...")
for cat in sorted(Path("plugins").iterdir()):
    if not cat.is_dir() or cat.name.startswith("_"): continue
    for pf in sorted(cat.glob("*.py")):
        if pf.name in SKIP: continue
        mod_path = f"plugins.{cat.name}.{pf.stem}"
        try:
            # Forcar reimport limpando cache
            if mod_path in sys.modules:
                del sys.modules[mod_path]
            mod = importlib.import_module(mod_path)
            plug = getattr(mod, "plugin", None)
            if plug:
                _routers.append((mod_path, plug))
                _ok += 1
        except Exception as e:
            _err += 1
            log.debug(f"skip {mod_path}: {e}")

log.info(f"Modulos importados: {_ok} OK / {_err} err")

# Passo 2: criar o app
app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1483 plugins de saude mental com IA",
    version="24.2.0",
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

@app.get("/health")
async def health():
    return {"status":"ok","version":"24.2.0","plugins":_ok,
            "erros":_err,"rotas":len(app.routes),
            "uptime":str(datetime.utcnow()-_start)}

@app.get("/ping")
async def ping():
    return {"pong":True,"ts":datetime.utcnow().isoformat()}

# Passo 3: registrar todos os plugins no app
log.info("Registrando plugins no app...")
_reg_ok = 0
_reg_err = 0
for mod_path, plug in _routers:
    try:
        plug.setup(app)
        _reg_ok += 1
    except Exception as e:
        _reg_err += 1
        log.debug(f"setup skip {mod_path}: {e}")

_ok = _reg_ok
log.info(f"Plugins registrados: {_reg_ok} OK / {_reg_err} err")
log.info(f"Rotas totais: {len(app.routes)}")
