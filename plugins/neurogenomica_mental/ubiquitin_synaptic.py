from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/ubiquitin_synaptic", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_ubiquitin_synaptic","s":"ativo","d":"Ubiquitin Synaptic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_ubiquitin_synaptic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
