from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/reconhecimento_voz", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_reconhecimento_voz","s":"ativo","d":"Reconhecimento Voz","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_reconhecimento_voz"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
