from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/sistemas/alertas_inteligentes", tags=["sistemas"])
@router.get("")
async def info():
    return JSONResponse({"p":"alertas_inteligentes","s":"ativo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "sistemas_alertas_inteligentes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
