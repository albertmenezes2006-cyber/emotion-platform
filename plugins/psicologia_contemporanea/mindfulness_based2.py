from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/mindfulness_based2", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_mindfulness_based2","s":"ativo","d":"Mindfulness Based2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_mindfulness_based2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
