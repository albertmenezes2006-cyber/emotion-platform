from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/emocao_tbi", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_emocao_tbi","s":"ativo","d":"Emocao Tbi","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_emocao_tbi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
