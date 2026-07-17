from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/insight_clinico", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__insight_clinico","s":"ativo","d":"Insight Clinico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__insight_clinico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
