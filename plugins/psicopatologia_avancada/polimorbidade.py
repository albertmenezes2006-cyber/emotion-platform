from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/polimorbidade", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__polimorbidade","s":"ativo","d":"Polimorbidade","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__polimorbidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
