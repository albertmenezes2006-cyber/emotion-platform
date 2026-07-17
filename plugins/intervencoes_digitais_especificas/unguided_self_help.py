from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/unguided_self_help", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_unguided_self_help","s":"ativo","d":"Unguided Self Help","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_unguided_self_help"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
