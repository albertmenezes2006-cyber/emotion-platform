from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/cardiac_physiology", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_cardiac_physiology","s":"ativo","d":"Cardiac Physiology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_cardiac_physiology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
