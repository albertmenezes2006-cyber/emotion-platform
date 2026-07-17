from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/startle_modulation", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_startle_modulation","s":"ativo","d":"Startle Modulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_startle_modulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
