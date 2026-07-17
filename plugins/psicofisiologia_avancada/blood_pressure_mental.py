from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/blood_pressure_mental", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_blood_pressure_mental","s":"ativo","d":"Blood Pressure Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_blood_pressure_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
