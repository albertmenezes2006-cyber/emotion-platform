
from plugins.plugin_base import PluginBase
from fastapi import APIRouter
import os, logging
logger = logging.getLogger(__name__)
router = APIRouter(prefix="/api/v1/dominio", tags=["Dominio"])
BASE   = os.getenv("BASE_URL","https://emotion-platform-albert.onrender.com")
DOM    = os.getenv("CUSTOM_DOMAIN","")

@router.get("/status")
async def status():
    return {"dominio_atual":BASE,"custom":DOM or "nao configurado","configurado":bool(DOM),
            "sugestoes":["emotionai.com.br","saudemental.app","emotionplatform.com.br"],
            "onde_comprar":{"registro_br":"https://registro.br","namecheap":"https://namecheap.com"}}

@router.get("/guia")
async def guia():
    return {"titulo":"Dominio Proprio - Guia","custo":"R$ 40/ano (.com.br)","tempo":"30min + 24h DNS",
            "passos":["1. Comprar em registro.br","2. DNS CNAME www -> emotion-platform-albert.onrender.com",
                      "3. Render -> Settings -> Custom Domain","4. SSL automatico (gratis)","5. BASE_URL=https://seudominio.com.br"]}

class DominioPlugin(PluginBase):
    name="dominio_config"; version="1.0.0"; description="Guia dominio"; category="utilidades"
    def setup(self,app): app.include_router(router); logger.info("[Dominio] OK")
    def health_check(self): return {"status":"healthy","dom":DOM or "padrao"}

plugin = DominioPlugin()
