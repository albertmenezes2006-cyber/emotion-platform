from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/validity_evidence", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_validity_evidence","s":"ativo","d":"Validity Evidence","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_validity_evidence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
