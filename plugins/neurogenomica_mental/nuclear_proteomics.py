from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/nuclear_proteomics", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_nuclear_proteomics","s":"ativo","d":"Nuclear Proteomics","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_nuclear_proteomics"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
