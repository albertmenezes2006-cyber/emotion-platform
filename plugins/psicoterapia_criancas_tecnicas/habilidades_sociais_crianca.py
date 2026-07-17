from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/habilidades_sociais_crian", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_habilidades_sociais_cr","s":"ativo","d":"Habilidades Sociais Crianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_habilidades_sociais_cr"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
