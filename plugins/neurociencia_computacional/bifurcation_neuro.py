from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/bifurcation_neuro", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_bifurcation_neuro","s":"ativo","d":"Bifurcation Neuro","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_bifurcation_neuro"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
