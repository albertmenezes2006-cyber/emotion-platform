from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/estavel", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__estavel","s":"ativo","d":"Estavel","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__estavel"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
