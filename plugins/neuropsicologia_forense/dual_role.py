from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/dual_role", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_dual_role","s":"ativo","d":"Dual Role","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_dual_role"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
