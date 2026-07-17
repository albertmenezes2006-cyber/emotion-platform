from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/collaborative_care3", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_collaborative_care3","s":"ativo","d":"Collaborative Care3","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_collaborative_care3"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
