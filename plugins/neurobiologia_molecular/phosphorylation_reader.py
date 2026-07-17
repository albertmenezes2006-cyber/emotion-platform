from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/phosphorylation_reader", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_phosphorylation_reader","s":"ativo","d":"Phosphorylation Reader","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_phosphorylation_reader"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
