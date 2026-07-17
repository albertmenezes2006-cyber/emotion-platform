from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/anything_goes", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_anything_goes","s":"ativo","d":"Anything Goes","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_anything_goes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
