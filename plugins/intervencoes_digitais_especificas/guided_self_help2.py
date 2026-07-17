from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/guided_self_help2", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_guided_self_help2","s":"ativo","d":"Guided Self Help2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_guided_self_help2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
