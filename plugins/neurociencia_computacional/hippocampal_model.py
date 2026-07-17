from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/hippocampal_model", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_hippocampal_model","s":"ativo","d":"Hippocampal Model","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_hippocampal_model"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
