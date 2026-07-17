from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/fenomenolo/tempo_vivido", tags=["fenomenologia_psicologica"])
@router.get("")
async def i():
    return JSONResponse({"p":"fenomenologia_p_tempo_vivido","s":"ativo","d":"Tempo Vivido","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "fenomenologia_p_tempo_vivido"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
