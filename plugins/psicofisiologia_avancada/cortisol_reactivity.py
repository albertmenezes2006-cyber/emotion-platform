from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/cortisol_reactivity", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_cortisol_reactivity","s":"ativo","d":"Cortisol Reactivity","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_cortisol_reactivity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
