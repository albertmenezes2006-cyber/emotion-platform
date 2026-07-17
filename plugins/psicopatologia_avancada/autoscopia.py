from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/autoscopia", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__autoscopia","s":"ativo","d":"Autoscopia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__autoscopia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
