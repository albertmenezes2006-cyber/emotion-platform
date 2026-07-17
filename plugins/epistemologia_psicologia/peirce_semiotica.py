from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/peirce_semiotica", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_peirce_semiotica","s":"ativo","d":"Peirce Semiotica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_peirce_semiotica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
