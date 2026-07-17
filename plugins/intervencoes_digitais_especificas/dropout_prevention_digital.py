from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/dropout_prevention_digita", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_dropout_prevention_dig","s":"ativo","d":"Dropout Prevention Digital","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_dropout_prevention_dig"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
