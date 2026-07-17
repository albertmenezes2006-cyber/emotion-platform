from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/laudo_neuropsico", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_laudo_neuropsico","s":"ativo","d":"Laudo Neuropsico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_laudo_neuropsico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
