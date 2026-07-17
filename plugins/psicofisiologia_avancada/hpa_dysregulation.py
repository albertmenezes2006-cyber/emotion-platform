from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/hpa_dysregulation", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_hpa_dysregulation","s":"ativo","d":"Hpa Dysregulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_hpa_dysregulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
