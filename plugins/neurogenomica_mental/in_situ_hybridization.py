from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/in_situ_hybridization", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_in_situ_hybridization","s":"ativo","d":"In Situ Hybridization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_in_situ_hybridization"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
