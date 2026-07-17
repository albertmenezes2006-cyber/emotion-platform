from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/multiscale_entropy", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_multiscale_entropy","s":"ativo","d":"Multiscale Entropy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_multiscale_entropy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
