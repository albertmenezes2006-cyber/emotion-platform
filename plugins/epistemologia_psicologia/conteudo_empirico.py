from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/conteudo_empirico", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_conteudo_empirico","s":"ativo","d":"Conteudo Empirico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_conteudo_empirico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
