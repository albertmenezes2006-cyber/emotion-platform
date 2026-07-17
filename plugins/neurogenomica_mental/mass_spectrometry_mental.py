from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurogenom/mass_spectrometry_mental", tags=["neurogenomica_mental"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurogenomica_m_mass_spectrometry_ment","s":"ativo","d":"Mass Spectrometry Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurogenomica_m_mass_spectrometry_ment"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
