from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/fenomenolo/presente_vivo", tags=["fenomenologia_psicologica"])
@router.get("")
async def i():
    return JSONResponse({"p":"fenomenologia_p_presente_vivo","s":"ativo","d":"Presente Vivo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "fenomenologia_p_presente_vivo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
