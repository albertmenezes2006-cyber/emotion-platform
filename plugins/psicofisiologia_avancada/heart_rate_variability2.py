from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/heart_rate_variability2", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_heart_rate_variability","s":"ativo","d":"Heart Rate Variability2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_heart_rate_variability"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
