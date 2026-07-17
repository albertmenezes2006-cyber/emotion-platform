from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/iact_tools", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_iact_tools","s":"ativo","d":"Iact Tools","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_iact_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
