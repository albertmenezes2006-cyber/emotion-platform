from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/retrograde_amnesia", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_retrograde_amnesia","s":"ativo","d":"Retrograde Amnesia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_retrograde_amnesia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
