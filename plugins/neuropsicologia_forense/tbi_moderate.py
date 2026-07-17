from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/tbi_moderate", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_tbi_moderate","s":"ativo","d":"Tbi Moderate","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_tbi_moderate"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
