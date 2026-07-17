from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/third_wave_therapies", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_third_wave_therapies","s":"ativo","d":"Third Wave Therapies","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_third_wave_therapies"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
