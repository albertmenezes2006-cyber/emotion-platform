from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/change_talk", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_change_talk","s":"ativo","d":"Change Talk","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_change_talk"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
