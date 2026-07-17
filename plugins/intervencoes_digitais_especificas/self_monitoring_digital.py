from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/self_monitoring_digital", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_self_monitoring_digita","s":"ativo","d":"Self Monitoring Digital","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_self_monitoring_digita"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
