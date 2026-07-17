from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/perito", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_perito","s":"ativo","d":"Perito","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_perito"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
