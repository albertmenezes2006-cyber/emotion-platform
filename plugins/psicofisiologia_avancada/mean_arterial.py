from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/mean_arterial", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_mean_arterial","s":"ativo","d":"Mean Arterial","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_mean_arterial"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
