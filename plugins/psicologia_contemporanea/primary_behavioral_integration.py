from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/primary_behavioral_integr", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_primary_behavioral_int","s":"ativo","d":"Primary Behavioral Integration","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_primary_behavioral_int"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
