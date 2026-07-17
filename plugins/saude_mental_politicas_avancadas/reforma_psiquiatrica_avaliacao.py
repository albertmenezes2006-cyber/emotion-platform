from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/reforma_psiquiatrica_aval", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_reforma_psiquiatrica_a","s":"ativo","d":"Reforma Psiquiatrica Avaliacao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_reforma_psiquiatrica_a"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
