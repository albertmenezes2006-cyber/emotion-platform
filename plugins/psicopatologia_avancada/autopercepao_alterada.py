from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/autopercepao_alterada", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__autopercepao_alterada","s":"ativo","d":"Autopercepao Alterada","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__autopercepao_alterada"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
