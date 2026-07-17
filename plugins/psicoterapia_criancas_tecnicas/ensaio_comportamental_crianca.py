from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/ensaio_comportamental_cri", tags=["psicoterapia_criancas_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_cr_ensaio_comportamental_","s":"ativo","d":"Ensaio Comportamental Crianca","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_cr_ensaio_comportamental_"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
