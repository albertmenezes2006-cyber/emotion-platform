"""
Plugin: Analytics — GA4 + Microsoft Clarity + eventos
Padrão: PluginBase + plugin = AnalyticsPlugin()
"""
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/analytics", tags=["analytics"])

GA4_ID     = os.getenv("GA4_ID", "G-XXXXXXXXXX")
CLARITY_ID = os.getenv("CLARITY_ID", "")
BASE_URL   = os.getenv("BASE_URL", "https://emotion-platform-albert.onrender.com")

@router.get("/status")
async def analytics_status():
    return {
        "status":  "online",
        "ga4":     {"id": GA4_ID,     "ativo": GA4_ID != "G-XXXXXXXXXX"},
        "clarity": {"id": CLARITY_ID, "ativo": bool(CLARITY_ID)},
        "eventos": ["avaliacao_emocional", "chat_ia", "ver_plano", "login", "cadastro"],
        "versao":  "1.0.0"
    }

@router.get("/snippet")
async def analytics_snippet():
    ga4_js = f"""
<!-- Google Analytics 4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script>
<script>
  window.dataLayer=window.dataLayer||[];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js',new Date());
  gtag('config','{GA4_ID}');
  window.trackEmotion = function(tipo,score){{
    gtag('event','avaliacao_emocional',{{event_category:'saude_mental',event_label:tipo,value:score}});
  }};
  window.trackChat = function(){{
    gtag('event','chat_ia',{{event_category:'engajamento'}});
  }};
</script>"""
    clarity_js = f"""
<!-- Microsoft Clarity -->
<script>
(function(c,l,a,r,i,t,y){{
  c[a]=c[a]||function(){{(c[a].q=c[a].q||[]).push(arguments)}};
  t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
  y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
}})(window,document,"clarity","script","{CLARITY_ID}");
</script>""" if CLARITY_ID else ""
    return {"ga4": ga4_js, "clarity": clarity_js}

@router.post("/evento")
async def registrar_evento(tipo: str, categoria: str = "geral", valor: int = 0):
    logger.info(f"[Analytics] evento: {tipo} | {categoria} | {valor}")
    return {"evento": tipo, "categoria": categoria, "valor": valor, "registrado": True}

class AnalyticsPlugin(PluginBase):
    name        = "analytics"
    version     = "1.0.0"
    description = "GA4 + Microsoft Clarity + eventos customizados"
    category    = "analytics"

    def setup(self, app):
        app.include_router(router)
        logger.info("[analytics] ✅ OK")

    def health_check(self):
        return {"status": "healthy", "plugin": self.name, "ga4": GA4_ID}

plugin = AnalyticsPlugin()
