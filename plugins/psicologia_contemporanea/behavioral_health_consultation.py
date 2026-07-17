from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/behavioral_health_consult", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_behavioral_health_cons","s":"ativo","d":"Behavioral Health Consultation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_behavioral_health_cons"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
