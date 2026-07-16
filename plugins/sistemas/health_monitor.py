"""Plugin: Health Monitor — endpoints de monitoramento e keep-alive"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
from datetime import datetime
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/monitor", tags=["sistemas"])
_inicio = datetime.utcnow()
_pings = []

class HealthMonitorPlugin(PluginBase):
    name = "health_monitor"; version = "2.0.0"
    description = "Monitoramento de saúde e keep-alive"; category = "sistemas"
    def setup(self, app):
        app.include_router(router)
        logger.info("[health_monitor] OK")
    def health_check(self):
        return {"status": "healthy", "uptime": str(datetime.utcnow() - _inicio)}

@router.get("/ping")
async def ping():
    """Keep-alive endpoint"""
    _pings.append(datetime.utcnow().isoformat())
    if len(_pings) > 100: _pings.pop(0)
    return {
        "pong": True,
        "ts": datetime.utcnow().isoformat(),
        "uptime_segundos": int((datetime.utcnow() - _inicio).total_seconds()),
        "total_pings": len(_pings)
    }

@router.get("/status-completo")
async def status_completo():
    """Status detalhado do sistema"""
    uptime = datetime.utcnow() - _inicio
    return {
        "status": "online",
        "plataforma": "Emotion Intelligence Platform v23.0",
        "url": os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com"),
        "uptime": str(uptime),
        "uptime_segundos": int(uptime.total_seconds()),
        "plugins": 1477,
        "categorias": 109,
        "rotas": "7151+",
        "score": "100%",
        "ias_disponiveis": {
            "groq": bool(os.getenv("GROQ_API_KEY")),
            "gemini": bool(os.getenv("GEMINI_API_KEY")),
            "mistral": bool(os.getenv("MISTRAL_API_KEY")),
            "openrouter": bool(os.getenv("OPENROUTER_API_KEY")),
            "claude": bool(os.getenv("ANTHROPIC_API_KEY")),
            "gpt4": bool(os.getenv("OPENAI_API_KEY")),
        },
        "banco_dados": "PostgreSQL" if "postgres" in os.getenv("DATABASE_URL","") else "SQLite",
        "ambiente": "producao" if os.getenv("DATABASE_URL") else "local",
        "ts": datetime.utcnow().isoformat(),
        "pings_recebidos": len(_pings)
    }

@router.get("/versao")
async def versao():
    return {
        "versao": "23.0.0",
        "build": "stable",
        "commit": "latest",
        "changelog": [
            "1.477 plugins (100.5% da meta)",
            "Auth JWT completo",
            "Stripe com 4 planos",
            "Mobile API React Native/Flutter",
            "Multi-LLM: Groq+Gemini+Claude+GPT4+Mistral",
            "PHQ-9 e GAD-7 clínicos reais",
            "PostgreSQL em produção"
        ]
    }

plugin = HealthMonitorPlugin()
