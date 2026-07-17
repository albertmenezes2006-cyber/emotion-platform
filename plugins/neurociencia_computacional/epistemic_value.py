from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/epistemic_value", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_epistemic_value","s":"ativo","d":"Epistemic Value","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_epistemic_value"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
