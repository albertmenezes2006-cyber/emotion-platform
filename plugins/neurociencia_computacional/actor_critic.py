from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/actor_critic", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_actor_critic","s":"ativo","d":"Actor Critic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_actor_critic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
