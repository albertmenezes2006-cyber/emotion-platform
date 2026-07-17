from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/care_coordination", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_care_coordination","s":"ativo","d":"Care Coordination","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_care_coordination"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
