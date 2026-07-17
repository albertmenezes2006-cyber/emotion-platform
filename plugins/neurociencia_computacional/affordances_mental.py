from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/affordances_mental", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_affordances_mental","s":"ativo","d":"Affordances Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_affordances_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
