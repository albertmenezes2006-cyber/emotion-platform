from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/ipRGC_mental", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_ipRGC_mental","s":"ativo","d":"Iprgc Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_ipRGC_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
