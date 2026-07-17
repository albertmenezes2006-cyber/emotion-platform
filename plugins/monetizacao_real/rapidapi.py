"""Plugin: RapidAPI marketplace internacional"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/rapidapi", tags=["Monetizacao"])
BASE   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def status():
    return {
        "status":          "online",
        "marketplace":     "https://rapidapi.com",
        "receita_estimada":"USD 100-1000/mes com 10 assinantes",
        "moeda":           "Dolares USD",
        "endpoints_para_vender": [
            BASE + "/api/v1/phq9-clinico/aplicar",
            BASE + "/api/v1/gad7-clinico/aplicar",
            BASE + "/api/v1/chat-ia/mensagem",
        ]
    }

@router.get("/guia")
async def guia():
    return {
        "titulo":  "Publicar sua API no RapidAPI",
        "url":     "https://rapidapi.com/provider",
        "passos": [
            "1. Criar conta em rapidapi.com/provider",
            "2. Add New API -> External API",
            f"3. Base URL: {BASE}",
            "4. Adicionar endpoints PHQ-9, GAD-7, Chat IA",
            "5. Definir precos: Free 10req, Basic $9.99, Pro $29.99",
            "6. Publicar e aguardar aprovacao",
        ],
        "planos_sugeridos": [
            {"nome": "Free",     "preco": "USD 0",    "requests": "10/mes"},
            {"nome": "Basic",    "preco": "USD 9.99", "requests": "1000/mes"},
            {"nome": "Pro",      "preco": "USD 29.99","requests": "10000/mes"},
            {"nome": "Business", "preco": "USD 99.99","requests": "ilimitado"},
        ],
        "vantagem": "Acesso a milhares de devs internacionais",
        "ganho_potencial": "USD 500-5000/mes"
    }

class RapidAPIPlugin(PluginBase):
    name = "rapidapi"
    version = "1.0.0"
    description = "RapidAPI marketplace USD"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info("[RapidAPI] OK")
    def health_check(self):
        return {"status": "healthy"}

plugin = RapidAPIPlugin()
