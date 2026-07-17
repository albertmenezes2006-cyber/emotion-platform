from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/duty_warn", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_duty_warn","s":"ativo","d":"Duty Warn","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_duty_warn"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
