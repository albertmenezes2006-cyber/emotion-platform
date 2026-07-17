"""Plugin: Google AdSense e alternativas de anuncios"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging

logger     = logging.getLogger(__name__)
router     = APIRouter(prefix="/api/v1/adsense", tags=["Monetizacao"])
ADSENSE_ID = os.getenv("ADSENSE_ID", "")
BASE       = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def status():
    return {
        "configurado":   bool(ADSENSE_ID),
        "adsense_id":    ADSENSE_ID or "Nao configurado",
        "receita_estimada": "R$ 50-500/mes com 1000 visitas/dia",
        "como_ativar": [
            "1. Acesse: https://adsense.google.com",
            "2. Cadastre: emotion-platform-albert.onrender.com",
            "3. Aguarde aprovacao (1-4 semanas)",
            "4. Copie Publisher ID: ca-pub-XXXXXXXXXXXXXXXXX",
            "5. Adicione no Render: ADSENSE_ID=ca-pub-XXXXXXXXXXXXXXXXX",
        ],
    }

@router.get("/guia")
async def guia():
    return {
        "titulo":  "Como ativar Google AdSense",
        "url":     "https://adsense.google.com",
        "requisitos": ["Site com conteudo original", "Minimo 50 visitas/dia", "Politica de privacidade"],
        "alternativas_imediatas": {
            "buymeacoffee": "buymeacoffee.com - aprovacao instantanea",
            "kofi":         "ko-fi.com - 0% taxa",
            "patreon":      "patreon.com - beneficios para apoiadores",
            "carbon_ads":   "carbonads.com - perfeito para devs",
        },
        "melhor_posicao_anuncios": ["Blog de saude mental", "Pagina de resultados PHQ-9", "Dashboard"]
    }

@router.get("/snippet")
async def snippet():
    if not ADSENSE_ID:
        return {"erro": "ADSENSE_ID nao configurado", "solucao": "Adicione ADSENSE_ID no Render"}
    script = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_ID}" crossorigin="anonymous"></script>'
    return {"script_head": script, "publisher_id": ADSENSE_ID}

class AdSensePlugin(PluginBase):
    name = "adsense"
    version = "1.0.0"
    description = "Google AdSense e alternativas"
    category = "monetizacao_real"
    def setup(self, app):
        app.include_router(router)
        logger.info(f"[AdSense] {'id='+ADSENSE_ID if ADSENSE_ID else 'aguardando aprovacao'}")
    def health_check(self):
        return {"status": "healthy", "adsense_ok": bool(ADSENSE_ID)}

plugin = AdSensePlugin()
