from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/direito_saude", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_direito_saude","s":"ativo","d":"Direito Saude","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_direito_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
