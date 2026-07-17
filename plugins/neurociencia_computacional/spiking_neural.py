from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/spiking_neural", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_spiking_neural","s":"ativo","d":"Spiking Neural","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_spiking_neural"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
