from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/theta_sequences", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_theta_sequences","s":"ativo","d":"Theta Sequences","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_theta_sequences"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
