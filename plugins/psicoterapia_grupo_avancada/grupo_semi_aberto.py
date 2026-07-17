from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/grupo_semi_aberto", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_grupo_semi_aberto","s":"ativo","d":"Grupo Semi Aberto","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_grupo_semi_aberto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
