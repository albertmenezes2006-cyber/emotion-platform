from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/dfa_hrv", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_dfa_hrv","s":"ativo","d":"Dfa Hrv","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_dfa_hrv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
