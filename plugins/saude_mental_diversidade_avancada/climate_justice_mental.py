from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/climate_justice_mental", tags=["saude_mental_diversidade_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_di_climate_justice_mental","s":"ativo","d":"Climate Justice Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_di_climate_justice_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
