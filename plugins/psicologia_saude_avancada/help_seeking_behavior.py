from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/help_seeking_behavior", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_help_seeking_behavior","s":"ativo","d":"Help Seeking Behavior","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_help_seeking_behavior"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
