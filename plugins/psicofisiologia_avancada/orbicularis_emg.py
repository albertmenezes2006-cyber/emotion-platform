from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/orbicularis_emg", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_orbicularis_emg","s":"ativo","d":"Orbicularis Emg","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_orbicularis_emg"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
