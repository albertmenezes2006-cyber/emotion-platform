from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/parkinson_forense", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_parkinson_forense","s":"ativo","d":"Parkinson Forense","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_parkinson_forense"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
