from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/contextual_therapies", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_contextual_therapies","s":"ativo","d":"Contextual Therapies","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_contextual_therapies"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
