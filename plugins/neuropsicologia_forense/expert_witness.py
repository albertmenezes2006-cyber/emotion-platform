from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/expert_witness", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_expert_witness","s":"ativo","d":"Expert Witness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_expert_witness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
