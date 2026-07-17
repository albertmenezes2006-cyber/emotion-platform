from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/intensive_outpatient", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_intensive_outpatient","s":"ativo","d":"Intensive Outpatient","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_intensive_outpatient"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
