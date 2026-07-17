from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/hf_hrv", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_hf_hrv","s":"ativo","d":"Hf Hrv","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_hf_hrv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
