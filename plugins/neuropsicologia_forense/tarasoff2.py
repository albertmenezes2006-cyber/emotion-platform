from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/tarasoff2", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_tarasoff2","s":"ativo","d":"Tarasoff2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_tarasoff2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
