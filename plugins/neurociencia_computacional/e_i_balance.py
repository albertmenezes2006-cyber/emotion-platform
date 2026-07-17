from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/e_i_balance", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_e_i_balance","s":"ativo","d":"E I Balance","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_e_i_balance"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
