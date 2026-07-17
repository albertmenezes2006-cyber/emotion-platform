from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/fourth_wave_cbt", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_fourth_wave_cbt","s":"ativo","d":"Fourth Wave Cbt","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_fourth_wave_cbt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
