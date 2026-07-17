from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/ancestralidade_sistemica", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_ancestralidade_sistemi","s":"ativo","d":"Ancestralidade Sistemica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_ancestralidade_sistemi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
