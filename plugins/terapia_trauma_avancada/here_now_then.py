from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapia_tr/here_now_then", tags=["terapia_trauma_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"terapia_trauma__here_now_then","s":"ativo","d":"Here Now Then","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapia_trauma__here_now_then"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
