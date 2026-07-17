from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/dhea_cortisol", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_dhea_cortisol","s":"ativo","d":"Dhea Cortisol","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_dhea_cortisol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
