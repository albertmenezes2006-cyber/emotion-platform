from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/aqui_agora_grupo", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_aqui_agora_grupo","s":"ativo","d":"Aqui Agora Grupo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_aqui_agora_grupo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
