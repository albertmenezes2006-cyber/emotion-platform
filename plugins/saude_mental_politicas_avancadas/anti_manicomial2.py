from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/anti_manicomial2", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_anti_manicomial2","s":"ativo","d":"Anti Manicomial2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_anti_manicomial2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
