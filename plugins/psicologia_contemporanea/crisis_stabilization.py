from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/crisis_stabilization", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_crisis_stabilization","s":"ativo","d":"Crisis Stabilization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_crisis_stabilization"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
