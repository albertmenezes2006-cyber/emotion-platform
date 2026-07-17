from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/clinical_vs_forensic", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_clinical_vs_forensic","s":"ativo","d":"Clinical Vs Forensic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_clinical_vs_forensic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
