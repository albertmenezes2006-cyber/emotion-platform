from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/cortisol_suppression", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_cortisol_suppression","s":"ativo","d":"Cortisol Suppression","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_cortisol_suppression"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
