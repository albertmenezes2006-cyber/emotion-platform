from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/prepulse_inhibition", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_prepulse_inhibition","s":"ativo","d":"Prepulse Inhibition","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_prepulse_inhibition"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
