from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/carneap_probabilidade", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_carneap_probabilidade","s":"ativo","d":"Carneap Probabilidade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_carneap_probabilidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
