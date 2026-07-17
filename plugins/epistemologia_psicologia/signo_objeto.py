from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/signo_objeto", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_signo_objeto","s":"ativo","d":"Signo Objeto","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_signo_objeto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
