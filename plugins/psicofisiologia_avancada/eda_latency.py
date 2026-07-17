from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/eda_latency", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_eda_latency","s":"ativo","d":"Eda Latency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_eda_latency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
