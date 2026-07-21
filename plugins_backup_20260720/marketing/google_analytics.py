
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/ga4", tags=["Marketing"])
GA4_ID = os.getenv("GA4_ID", "")
BASE   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def ga4_status():
    return {
        "configurado":      bool(GA4_ID),
        "ga4_id":           GA4_ID or "Adicione GA4_ID no Render",
        "como_configurar":  "analytics.google.com -> copie G-XXXXXXXXXX -> Render env vars",
        "dashboard":        "https://analytics.google.com"
    }

@router.get("/snippet")
async def ga4_snippet():
    if not GA4_ID:
        return {"erro": "GA4_ID nao configurado", "solucao": "Adicione GA4_ID no Render"}
    return {
        "ga4_id":  GA4_ID,
        "snippet": f"<script async src=https://www.googletagmanager.com/gtag/js?id={GA4_ID}></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{GA4_ID}');</script>"
    }

@router.get("/eventos")
async def ga4_eventos():
    return {"eventos": ["avaliacao","chat_ia","ver_plano","cadastro","login"],"dashboard":"https://analytics.google.com"}

@router.get("/instrucoes")
async def instrucoes():
    return {
        "passo_1": "Acesse https://analytics.google.com",
        "passo_2": "Criar conta -> Nome: Emotion Platform",
        "passo_3": "Propriedade -> Web -> URL: emotion-platform-albert.onrender.com",
        "passo_4": "Copie o ID: G-XXXXXXXXXX",
        "passo_5": "Render -> Environment -> GA4_ID = G-XXXXXXXXXX",
        "passo_6": "Deploy e pronto!"
    }

class GoogleAnalyticsPlugin(PluginBase):
    name="google_analytics"; version="1.0.0"
    description="Google Analytics 4"; category="marketing"
    def setup(self, app):
        app.include_router(router)
        status = "id="+GA4_ID if GA4_ID else "aguardando GA4_ID no Render"
        logger.info(f"[GA4] {status}")
    def health_check(self):
        return {"status":"healthy","ga4_ok":bool(GA4_ID),"ga4_id":GA4_ID or "nao configurado"}

plugin = GoogleAnalyticsPlugin()
