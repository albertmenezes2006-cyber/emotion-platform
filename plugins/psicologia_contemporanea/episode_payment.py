from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/episode_payment", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_episode_payment","s":"ativo","d":"Episode Payment","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_episode_payment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
