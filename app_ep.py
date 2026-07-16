#!/usr/bin/env python3
"""
app_ep.py — Servidor APENAS dos plugins (sem conflito com main.py)
Roda em porta separada: uvicorn app_ep:app --port 8001
No Render: usar este como ponto de entrada
"""
import os, logging
logging.basicConfig(level=logging.INFO)

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Emotion Intelligence Platform — Plugins v23",
    description="1477 plugins de saúde mental com IA",
    version="23.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Static files
try:
    if os.path.exists("static"):
        app.mount("/static", StaticFiles(directory="static"), name="static")
except Exception:
    pass

# Carregar todos os plugins
from plugins.loader import load_all_plugins
ok, err = load_all_plugins(app)
logging.getLogger(__name__).info(f"✅ {ok} plugins carregados ({err} ignorados)")
