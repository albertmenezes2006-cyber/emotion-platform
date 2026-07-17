from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/equine_therapy2", tags=["psicologia_ambiental_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_ambi_equine_therapy2","s":"ativo","d":"Equine Therapy2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_ambi_equine_therapy2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
