#!/usr/bin/env python3
"""Health check avancado com detalhes"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
import httpx
import os
from datetime import datetime

router = APIRouter(prefix="/api/v1/health", tags=["Health"])

@router.get("/detalhado")
async def health_detalhado():
    checks = {}
    # Check DB
    try:
        db_url = os.getenv("DATABASE_URL", "")
        checks["database"] = "configurado" if db_url else "nao_configurado"
    except:
        checks["database"] = "erro"
    # Check APIs IA
    checks["groq"] = "configurado" if os.getenv("GROQ_API_KEY") else "nao_configurado"
    checks["gemini"] = "configurado" if os.getenv("GEMINI_API_KEY") else "nao_configurado"
    checks["mistral"] = "configurado" if os.getenv("MISTRAL_API_KEY") else "nao_configurado"
    # Check Stripe
    checks["stripe"] = "configurado" if os.getenv("STRIPE_SECRET_KEY") else "nao_configurado"
    # Check Telegram
    checks["telegram"] = "configurado" if os.getenv("TELEGRAM_TOKEN") else "nao_configurado"
    status_geral = "ok" if all(
        v != "erro" for v in checks.values()
    ) else "degradado"
    return JSONResponse({
        "status": status_geral,
        "timestamp": datetime.utcnow().isoformat(),
        "versao": "24.4.0",
        "checks": checks,
        "ambiente": os.getenv("RENDER", "local")
    })

@router.get("/ping-externo")
async def ping_externo():
    try:
        async with httpx.AsyncClient(timeout=5) as client:
            r = await client.get("https://httpbin.org/get")
            return {"internet": "ok", "status": r.status_code}
    except:
        return {"internet": "erro"}

class HealthAdvPlugin(PluginBase):
    name = "health_avancado"
    def setup(self, app):
        app.include_router(router)

plugin = HealthAdvPlugin()
