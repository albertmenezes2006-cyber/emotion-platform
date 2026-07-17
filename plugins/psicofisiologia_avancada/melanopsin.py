from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/melanopsin", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_melanopsin","s":"ativo","d":"Melanopsin","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_melanopsin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
