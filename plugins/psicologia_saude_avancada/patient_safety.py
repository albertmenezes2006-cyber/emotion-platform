from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/patient_safety", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_patient_safety","s":"ativo","d":"Patient Safety","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_patient_safety"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
