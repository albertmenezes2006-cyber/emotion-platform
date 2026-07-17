from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/papeis_sistemicos", tags=["psicoterapia_grupo_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_gr_papeis_sistemicos","s":"ativo","d":"Papeis Sistemicos","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_gr_papeis_sistemicos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
