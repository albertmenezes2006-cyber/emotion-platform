from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/perspectiva_multigeracion", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_perspectiva_multigerac","s":"ativo","d":"Perspectiva Multigeracional","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_perspectiva_multigerac"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
