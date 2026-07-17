from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/variabilidade", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__variabilidade","s":"ativo","d":"Variabilidade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__variabilidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
