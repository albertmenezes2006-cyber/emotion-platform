#!/usr/bin/env python3
"""
Emotion Intelligence Platform v24.0
Entry point principal — carrega todos os 1477 plugins
"""
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

logger.info("🚀 Emotion Intelligence Platform v24.0 iniciando...")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Emotion Intelligence Platform",
    description="1477 plugins de saúde mental com IA — PHQ-9, GAD-7, Chat IA, Diário, Agenda",
    version="24.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static files
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
    logger.info(f"✅ {ok} plugins carregados ({err} ignorados)")
    logger.info(f"✅ {len(app.routes)} rotas totais")
except Exception as e:
    logger.error(f"❌ Erro ao carregar plugins: {e}")

logger.info("🎯 Plataforma pronta!")
