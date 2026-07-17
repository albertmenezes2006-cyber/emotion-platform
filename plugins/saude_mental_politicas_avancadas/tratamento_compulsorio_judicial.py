from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/tratamento_compulsorio_ju", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_tratamento_compulsorio","s":"ativo","d":"Tratamento Compulsorio Judicial","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_tratamento_compulsorio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
