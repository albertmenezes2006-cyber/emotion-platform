from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/population_health_mental", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_population_health_ment","s":"ativo","d":"Population Health Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_population_health_ment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
