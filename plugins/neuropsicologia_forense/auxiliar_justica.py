from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/auxiliar_justica", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_auxiliar_justica","s":"ativo","d":"Auxiliar Justica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_auxiliar_justica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
