from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/burden_disease", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__burden_disease","s":"ativo","d":"Burden Disease","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__burden_disease"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
