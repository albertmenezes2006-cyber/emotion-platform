from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/aprendizado_imitativo", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_aprendizado_imitativo","s":"ativo","d":"Aprendizado Imitativo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_aprendizado_imitativo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
