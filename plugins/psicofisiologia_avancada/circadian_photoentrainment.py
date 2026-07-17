from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/circadian_photoentrainmen", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_circadian_photoentrain","s":"ativo","d":"Circadian Photoentrainment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_circadian_photoentrain"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
