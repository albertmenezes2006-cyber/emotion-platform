from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/avaliacao_forense_neuro", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_avaliacao_forense_neur","s":"ativo","d":"Avaliacao Forense Neuro","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_avaliacao_forense_neur"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
