from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/processo_grupo_conteudo", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_processo_grupo_conteud","s":"ativo","d":"Processo Grupo Conteudo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_processo_grupo_conteud"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
