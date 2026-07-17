from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/probabilidade_frequentist", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_probabilidade_frequent","s":"ativo","d":"Probabilidade Frequentista","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_probabilidade_frequent"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
