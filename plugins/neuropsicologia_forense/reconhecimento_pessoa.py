from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/reconhecimento_pessoa", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_reconhecimento_pessoa","s":"ativo","d":"Reconhecimento Pessoa","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_reconhecimento_pessoa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
