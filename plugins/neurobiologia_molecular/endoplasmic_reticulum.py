from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/endoplasmic_reticulum", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_endoplasmic_reticulum","s":"ativo","d":"Endoplasmic Reticulum","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_endoplasmic_reticulum"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
