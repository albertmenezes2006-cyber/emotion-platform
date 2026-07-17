from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/fenomenolo/consciencia_interna", tags=["fenomenologia_psicologica"])
@router.get("")
async def i():
    return JSONResponse({"p":"fenomenologia_p_consciencia_interna","s":"ativo","d":"Consciencia Interna","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "fenomenologia_p_consciencia_interna"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
