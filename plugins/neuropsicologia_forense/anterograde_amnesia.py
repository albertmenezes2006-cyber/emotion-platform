from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/anterograde_amnesia", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_anterograde_amnesia","s":"ativo","d":"Anterograde Amnesia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_anterograde_amnesia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
