from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapia_tr/emotional_parts", tags=["terapia_trauma_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"terapia_trauma__emotional_parts","s":"ativo","d":"Emotional Parts","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapia_trauma__emotional_parts"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
