from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/eyewitness_adulto", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_eyewitness_adulto","s":"ativo","d":"Eyewitness Adulto","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_eyewitness_adulto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
