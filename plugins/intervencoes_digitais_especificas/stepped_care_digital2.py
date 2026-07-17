from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/stepped_care_digital2", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_stepped_care_digital2","s":"ativo","d":"Stepped Care Digital2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_stepped_care_digital2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
