from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/white_coat", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_white_coat","s":"ativo","d":"White Coat","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_white_coat"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
