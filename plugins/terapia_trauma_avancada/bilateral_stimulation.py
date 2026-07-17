from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapia_tr/bilateral_stimulation", tags=["terapia_trauma_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"terapia_trauma__bilateral_stimulation","s":"ativo","d":"Bilateral Stimulation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapia_trauma__bilateral_stimulation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
