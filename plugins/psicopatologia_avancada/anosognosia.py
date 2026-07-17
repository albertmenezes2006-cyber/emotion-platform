from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/anosognosia", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__anosognosia","s":"ativo","d":"Anosognosia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__anosognosia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
