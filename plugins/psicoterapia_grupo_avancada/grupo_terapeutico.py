from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/grupo_terapeutico", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_grupo_terapeutico","s":"ativo","d":"Grupo Terapeutico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_grupo_terapeutico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
