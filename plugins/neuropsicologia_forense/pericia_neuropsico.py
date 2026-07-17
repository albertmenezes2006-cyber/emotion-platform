from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/pericia_neuropsico", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_pericia_neuropsico","s":"ativo","d":"Pericia Neuropsico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_pericia_neuropsico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
