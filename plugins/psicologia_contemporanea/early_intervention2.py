from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/early_intervention2", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_early_intervention2","s":"ativo","d":"Early Intervention2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_early_intervention2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
