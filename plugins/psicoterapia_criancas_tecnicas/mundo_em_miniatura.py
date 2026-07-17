from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/mundo_em_miniatura", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_mundo_em_miniatura","s":"ativo","d":"Mundo Em Miniatura","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_mundo_em_miniatura"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
