from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/tau_phosphorylation", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_tau_phosphorylation","s":"ativo","d":"Tau Phosphorylation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_tau_phosphorylation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
