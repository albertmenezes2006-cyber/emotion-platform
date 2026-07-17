from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/terapia_cognitiva_crianca", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_terapia_cognitiva_cria","s":"ativo","d":"Terapia Cognitiva Crianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_terapia_cognitiva_cria"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
