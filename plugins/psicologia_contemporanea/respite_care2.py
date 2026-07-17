from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/respite_care2", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_respite_care2","s":"ativo","d":"Respite Care2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_respite_care2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
