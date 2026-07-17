from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/limits_confidentiality", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_limits_confidentiality","s":"ativo","d":"Limits Confidentiality","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_limits_confidentiality"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
