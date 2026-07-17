from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/funcionamento_global", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__funcionamento_global","s":"ativo","d":"Funcionamento Global","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__funcionamento_global"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
