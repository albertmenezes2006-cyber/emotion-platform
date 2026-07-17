from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/resolucao_problema_crianc", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_resolucao_problema_cri","s":"ativo","d":"Resolucao Problema Crianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_resolucao_problema_cri"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
