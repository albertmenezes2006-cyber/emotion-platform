from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/sharp_wave_ripple", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_sharp_wave_ripple","s":"ativo","d":"Sharp Wave Ripple","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_sharp_wave_ripple"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
