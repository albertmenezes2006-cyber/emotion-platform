from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/rename_mental", tags=["saude_mental_politicas_avancadas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_po_rename_mental","s":"ativo","d":"Rename Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_po_rename_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
