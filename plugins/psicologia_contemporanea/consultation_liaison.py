from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/consultation_liaison", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_consultation_liaison","s":"ativo","d":"Consultation Liaison","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_consultation_liaison"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
