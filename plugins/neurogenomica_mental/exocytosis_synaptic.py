from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/exocytosis_synaptic", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_exocytosis_synaptic","s":"ativo","d":"Exocytosis Synaptic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_exocytosis_synaptic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
