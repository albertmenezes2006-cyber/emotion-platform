from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/baroreflex_sensitivity", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_baroreflex_sensitivity","s":"ativo","d":"Baroreflex Sensitivity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_baroreflex_sensitivity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
