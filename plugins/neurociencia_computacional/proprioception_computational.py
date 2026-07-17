from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/proprioception_computatio", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_proprioception_computa","s":"ativo","d":"Proprioception Computational","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_proprioception_computa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
