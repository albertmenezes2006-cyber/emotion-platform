from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/lc3_autophagy", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_lc3_autophagy","s":"ativo","d":"Lc3 Autophagy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_lc3_autophagy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
