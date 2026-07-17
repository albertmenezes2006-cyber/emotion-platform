from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/phasic_eda", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_phasic_eda","s":"ativo","d":"Phasic Eda","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_phasic_eda"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
