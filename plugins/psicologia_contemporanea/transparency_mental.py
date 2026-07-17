from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/transparency_mental", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_transparency_mental","s":"ativo","d":"Transparency Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_transparency_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
