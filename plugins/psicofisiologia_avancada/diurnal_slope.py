from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/diurnal_slope", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_diurnal_slope","s":"ativo","d":"Diurnal Slope","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_diurnal_slope"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
