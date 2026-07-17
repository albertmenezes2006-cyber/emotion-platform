from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/fenomenolo/mundo_vida_lebenswelt", tags=["fenomenologia_psicologica"])
@router.get("")
async def i():
    return JSONResponse({"p":"fenomenologia_p_mundo_vida_lebenswelt","s":"ativo","d":"Mundo Vida Lebenswelt","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "fenomenologia_p_mundo_vida_lebenswelt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
