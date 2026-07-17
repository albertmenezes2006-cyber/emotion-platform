from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/psicopatologia_integrativ", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__psicopatologia_integra","s":"ativo","d":"Psicopatologia Integrativa","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__psicopatologia_integra"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
