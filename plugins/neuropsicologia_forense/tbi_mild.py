from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/tbi_mild", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_tbi_mild","s":"ativo","d":"Tbi Mild","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_tbi_mild"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
