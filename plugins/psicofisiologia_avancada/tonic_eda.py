from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/tonic_eda", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_tonic_eda","s":"ativo","d":"Tonic Eda","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_tonic_eda"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
