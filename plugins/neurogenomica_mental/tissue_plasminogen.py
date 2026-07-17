from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/tissue_plasminogen", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_tissue_plasminogen","s":"ativo","d":"Tissue Plasminogen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_tissue_plasminogen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
