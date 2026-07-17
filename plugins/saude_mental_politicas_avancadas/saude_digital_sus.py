from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/saude_digital_sus", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_saude_digital_sus","s":"ativo","d":"Saude Digital Sus","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_saude_digital_sus"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
