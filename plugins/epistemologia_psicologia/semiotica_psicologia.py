from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/semiotica_psicologia", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_semiotica_psicologia","s":"ativo","d":"Semiotica Psicologia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_semiotica_psicologia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
