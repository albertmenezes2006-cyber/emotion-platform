from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/warm_handoff", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_warm_handoff","s":"ativo","d":"Warm Handoff","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_warm_handoff"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
