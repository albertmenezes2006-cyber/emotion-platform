from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapia_tr/trust_trauma", tags=["terapia_trauma_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"terapia_trauma__trust_trauma","s":"ativo","d":"Trust Trauma","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapia_trauma__trust_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
