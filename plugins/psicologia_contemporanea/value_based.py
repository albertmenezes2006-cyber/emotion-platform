from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/value_based", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_value_based","s":"ativo","d":"Value Based","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_value_based"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
