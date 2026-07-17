from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/unified_protocol3", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_unified_protocol3","s":"ativo","d":"Unified Protocol3","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_unified_protocol3"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
