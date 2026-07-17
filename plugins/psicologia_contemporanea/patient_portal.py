from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/patient_portal", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_patient_portal","s":"ativo","d":"Patient Portal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_patient_portal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
