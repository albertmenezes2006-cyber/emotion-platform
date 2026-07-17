from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/electrodermal_activity", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_electrodermal_activity","s":"ativo","d":"Electrodermal Activity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_electrodermal_activity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
