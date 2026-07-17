from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/avaliacao_capacidade", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_avaliacao_capacidade","s":"ativo","d":"Avaliacao Capacidade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_avaliacao_capacidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
