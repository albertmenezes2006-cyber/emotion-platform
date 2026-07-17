
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging, time
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/uptime", tags=["Marketing"])
START  = time.time()
BASE   = os.getenv("BASE_URL","https://emotion-platform-albert.onrender.com")

@router.get("/ping")
async def ping():
    return {"status":"online","ts":int(time.time()),"msg":"pong"}

@router.get("/status")
async def status():
    seg   = int(time.time()-START)
    horas = seg//3600
    mins  = (seg%3600)//60
    return {
        "status":    "online",
        "uptime":    f"{horas}h {mins}m",
        "monitores": {
            "health":    BASE+"/health",
            "ping":      BASE+"/api/v1/uptime/ping",
            "avaliacao": BASE+"/app/avaliacao"
        },
        "uptimerobot": "https://uptimerobot.com",
        "plano":       "FREE - 50 monitores - intervalo 5min"
    }

@router.get("/instrucoes")
async def instrucoes():
    return {
        "servico":   "UptimeRobot",
        "url":       "https://uptimerobot.com",
        "plano":     "FREE",
        "beneficio": "Render free dorme apos 15min. UptimeRobot evita isso fazendo ping a cada 5min.",
        "passos": [
            "1. Criar conta gratis em uptimerobot.com",
            "2. Add New Monitor -> HTTP(s)",
            f"3. URL: {BASE}/health",
            "4. Interval: 5 minutes",
            "5. Salvar - pronto!",
            f"6. Extra: monitor {BASE}/api/v1/uptime/ping"
        ]
    }

class UptimePlugin(PluginBase):
    name="uptime_monitor"; version="1.0.0"
    description="UptimeRobot monitor"; category="marketing"
    def setup(self, app):
        app.include_router(router)
        logger.info("[Uptime] OK")
    def health_check(self):
        return {"status":"healthy","uptime_s":int(time.time()-START)}

plugin = UptimePlugin()
