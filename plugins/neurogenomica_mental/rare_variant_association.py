from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/rare_variant_association", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_rare_variant_associati","s":"ativo","d":"Rare Variant Association","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_rare_variant_associati"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
