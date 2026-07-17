from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/abduction", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_abduction","s":"ativo","d":"Abduction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_abduction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
