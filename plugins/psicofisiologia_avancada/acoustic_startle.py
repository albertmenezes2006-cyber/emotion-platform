from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/acoustic_startle", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_acoustic_startle","s":"ativo","d":"Acoustic Startle","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_acoustic_startle"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
