from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/duty_protect", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_duty_protect","s":"ativo","d":"Duty Protect","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_duty_protect"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
