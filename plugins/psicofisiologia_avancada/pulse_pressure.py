from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/pulse_pressure", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_pulse_pressure","s":"ativo","d":"Pulse Pressure","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_pulse_pressure"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
