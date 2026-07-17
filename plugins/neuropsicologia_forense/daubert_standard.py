from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/daubert_standard", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_daubert_standard","s":"ativo","d":"Daubert Standard","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_daubert_standard"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
