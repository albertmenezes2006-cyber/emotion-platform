from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/caspase_mental", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_caspase_mental","s":"ativo","d":"Caspase Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_caspase_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
