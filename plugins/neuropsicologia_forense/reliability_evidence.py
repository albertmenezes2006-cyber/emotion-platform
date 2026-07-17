from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/reliability_evidence", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_reliability_evidence","s":"ativo","d":"Reliability Evidence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_reliability_evidence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
