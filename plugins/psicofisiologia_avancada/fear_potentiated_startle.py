from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/fear_potentiated_startle", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_fear_potentiated_start","s":"ativo","d":"Fear Potentiated Startle","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_fear_potentiated_start"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
