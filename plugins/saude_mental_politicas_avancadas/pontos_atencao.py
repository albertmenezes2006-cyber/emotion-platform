from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/pontos_atencao", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_pontos_atencao","s":"ativo","d":"Pontos Atencao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_pontos_atencao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
