from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/canal_calcio", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_canal_calcio","s":"ativo","d":"Canal Calcio","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_canal_calcio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
