from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/tecnicas_socializacao", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_tecnicas_socializacao","s":"ativo","d":"Tecnicas Socializacao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_tecnicas_socializacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
