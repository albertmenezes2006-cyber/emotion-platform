from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/fenomenolo/intencionalidade_de_ato", tags=["fenomenologia_psicologica"])
@router.get("")
async def i():
    return JSONResponse({"p":"fenomenologia_p_intencionalidade_de_at","s":"ativo","d":"Intencionalidade De Ato","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "fenomenologia_p_intencionalidade_de_at"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
