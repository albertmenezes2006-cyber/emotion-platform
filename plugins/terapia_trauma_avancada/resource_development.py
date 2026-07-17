from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/terapia_tr/resource_development", tags=["terapia_trauma_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"terapia_trauma__resource_development","s":"ativo","d":"Resource Development","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "terapia_trauma__resource_development"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
