from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/metaforas_crianca", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_metaforas_crianca","s":"ativo","d":"Metaforas Crianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_metaforas_crianca"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
