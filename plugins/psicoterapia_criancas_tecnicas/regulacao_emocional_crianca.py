from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/regulacao_emocional_crian", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_regulacao_emocional_cr","s":"ativo","d":"Regulacao Emocional Crianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_regulacao_emocional_cr"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
