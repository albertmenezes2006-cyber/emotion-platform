from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/ludoterapia_diretiva", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_ludoterapia_diretiva","s":"ativo","d":"Ludoterapia Diretiva","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_ludoterapia_diretiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
