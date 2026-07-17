from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/judicializacao_saude", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_judicializacao_saude","s":"ativo","d":"Judicializacao Saude","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_judicializacao_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
