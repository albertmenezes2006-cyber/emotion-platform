from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/imbct_mindfulness", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_imbct_mindfulness","s":"ativo","d":"Imbct Mindfulness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_imbct_mindfulness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
