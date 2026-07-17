from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/allostatic_overload", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_allostatic_overload","s":"ativo","d":"Allostatic Overload","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_allostatic_overload"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
