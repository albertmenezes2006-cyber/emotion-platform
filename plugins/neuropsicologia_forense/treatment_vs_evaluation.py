from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/treatment_vs_evaluation", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_treatment_vs_evaluatio","s":"ativo","d":"Treatment Vs Evaluation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_treatment_vs_evaluatio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
