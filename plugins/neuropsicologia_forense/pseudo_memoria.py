from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/pseudo_memoria", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_pseudo_memoria","s":"ativo","d":"Pseudo Memoria","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_pseudo_memoria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
