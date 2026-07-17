from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/capacidade_processual", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_capacidade_processual","s":"ativo","d":"Capacidade Processual","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_capacidade_processual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
