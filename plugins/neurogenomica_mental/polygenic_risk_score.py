from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/polygenic_risk_score", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_polygenic_risk_score","s":"ativo","d":"Polygenic Risk Score","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_polygenic_risk_score"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
