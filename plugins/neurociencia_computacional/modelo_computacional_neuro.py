from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/modelo_computacional_neur", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_modelo_computacional_n","s":"ativo","d":"Modelo Computacional Neuro","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_modelo_computacional_n"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
