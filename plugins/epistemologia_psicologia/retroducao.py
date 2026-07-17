from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/retroducao", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_retroducao","s":"ativo","d":"Retroducao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_retroducao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
