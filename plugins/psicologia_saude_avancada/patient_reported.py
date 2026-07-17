from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/patient_reported", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_patient_reported","s":"ativo","d":"Patient Reported","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_patient_reported"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
