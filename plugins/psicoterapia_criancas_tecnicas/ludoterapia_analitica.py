from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/ludoterapia_analitica", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_ludoterapia_analitica","s":"ativo","d":"Ludoterapia Analitica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_ludoterapia_analitica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
