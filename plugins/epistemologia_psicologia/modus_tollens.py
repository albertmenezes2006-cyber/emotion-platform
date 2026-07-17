from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/modus_tollens", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_modus_tollens","s":"ativo","d":"Modus Tollens","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_modus_tollens"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
