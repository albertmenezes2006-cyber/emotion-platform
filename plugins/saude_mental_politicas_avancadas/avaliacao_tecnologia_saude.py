from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/avaliacao_tecnologia_saud", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_avaliacao_tecnologia_s","s":"ativo","d":"Avaliacao Tecnologia Saude","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_avaliacao_tecnologia_s"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
