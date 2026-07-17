from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/personalidade_tbi", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_personalidade_tbi","s":"ativo","d":"Personalidade Tbi","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_personalidade_tbi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
