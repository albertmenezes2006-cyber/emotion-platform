from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/transtorno_mental", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__transtorno_mental","s":"ativo","d":"Transtorno Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__transtorno_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
