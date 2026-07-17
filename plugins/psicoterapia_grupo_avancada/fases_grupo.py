from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/fases_grupo", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_fases_grupo","s":"ativo","d":"Fases Grupo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_fases_grupo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
