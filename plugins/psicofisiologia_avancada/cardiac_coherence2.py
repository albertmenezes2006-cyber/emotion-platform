from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/cardiac_coherence2", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_cardiac_coherence2","s":"ativo","d":"Cardiac Coherence2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_cardiac_coherence2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
