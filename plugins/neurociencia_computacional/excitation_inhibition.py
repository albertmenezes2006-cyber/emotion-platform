from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/excitation_inhibition", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_excitation_inhibition","s":"ativo","d":"Excitation Inhibition","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_excitation_inhibition"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
