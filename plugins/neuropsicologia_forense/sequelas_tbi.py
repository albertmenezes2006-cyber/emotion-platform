from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/sequelas_tbi", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_sequelas_tbi","s":"ativo","d":"Sequelas Tbi","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_sequelas_tbi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
