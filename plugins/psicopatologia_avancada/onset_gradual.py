from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/onset_gradual", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__onset_gradual","s":"ativo","d":"Onset Gradual","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__onset_gradual"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
