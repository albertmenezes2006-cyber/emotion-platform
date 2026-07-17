from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/desduplamento", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__desduplamento","s":"ativo","d":"Desduplamento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__desduplamento"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
