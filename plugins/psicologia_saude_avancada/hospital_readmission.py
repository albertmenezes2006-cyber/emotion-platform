from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/hospital_readmission", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_hospital_readmission","s":"ativo","d":"Hospital Readmission","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_hospital_readmission"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
