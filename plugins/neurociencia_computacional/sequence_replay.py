from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/sequence_replay", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_sequence_replay","s":"ativo","d":"Sequence Replay","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_sequence_replay"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
