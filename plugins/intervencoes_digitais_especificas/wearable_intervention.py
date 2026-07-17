from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/wearable_intervention", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_wearable_intervention","s":"ativo","d":"Wearable Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_wearable_intervention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
