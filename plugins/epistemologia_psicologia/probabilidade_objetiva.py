from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/probabilidade_objetiva", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_probabilidade_objetiva","s":"ativo","d":"Probabilidade Objetiva","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_probabilidade_objetiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
