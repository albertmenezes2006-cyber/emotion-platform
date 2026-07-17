from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/rate_coding", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_rate_coding","s":"ativo","d":"Rate Coding","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_rate_coding"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
