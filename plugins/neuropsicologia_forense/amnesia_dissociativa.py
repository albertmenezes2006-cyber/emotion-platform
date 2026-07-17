from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/amnesia_dissociativa", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_amnesia_dissociativa","s":"ativo","d":"Amnesia Dissociativa","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_amnesia_dissociativa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
