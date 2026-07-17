#!/usr/bin/env python3
"""Emotion Intelligence Platform v24.4.0 - MAXIMO DESEMPENHO"""
import os
import importlib
import sys
import logging
import gc
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware
from datetime import datetime

# Aumentar limites
sys.setrecursionlimit(50000)

logging.basicConfig(
    level=logging.WARNING,
    format="%(asctime)s %(levelname)s: %(message)s"
)
log = logging.getLogger("ep")

app = FastAPI(
    title="Emotion Intelligence Platform",
    description="Plataforma de saude mental com IA - Maximo Desempenho",
    version="24.4.0",
    docs_url=None,
    redoc_url=None,
    openapi_url=None,
)

# Middlewares essenciais
app.add_middleware(CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
app.add_middleware(GZipMiddleware, minimum_size=500)

# Static files
try:
    from fastapi.staticfiles import StaticFiles
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass

_start = datetime.utcnow()
_ok = 0
_err = 0
_nomes_vistos = set()

@app.api_route("/health", methods=["GET", "HEAD"])
async def health():
    return {
        "status": "ok",
        "version": "24.4.0",
        "plugins": _ok,
        "erros": _err,
        "rotas": len(app.routes),
        "uptime": str(datetime.utcnow() - _start)
    }

@app.api_route("/ping", methods=["GET", "HEAD"])
async def ping():
    return {"pong": True, "ts": datetime.utcnow().isoformat()}

# Carregar plugins com deduplicacao e otimizacao de memoria
SKIP = {"__init__.py", "loader.py", "plugin_base.py", "db_manager.py"}

log.warning("Carregando plugins - MODO MAXIMO...")

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
                # Evitar duplicados pelo nome
                nome = getattr(plug, "name", mod_path)
                if nome in _nomes_vistos:
                    continue
                _nomes_vistos.add(nome)
                plug.setup(app)
                _ok += 1
                # Liberar memoria do modulo apos setup
                del plug
        except RecursionError:
            _err += 1
        except SyntaxError as e:
            _err += 1
            log.debug(f"SyntaxError {mod_path}: {e}")
        except Exception as e:
            _err += 1
            log.debug(f"skip {mod_path}: {type(e).__name__}")
        finally:
            # GC periodico para liberar memoria
            if (_ok + _err) % 500 == 0:
                gc.collect()

gc.collect()
log.warning(f"MAXIMO: {_ok} plugins / {_err} erros / {len(app.routes)} rotas")
