from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/aryl_hydrocarbon", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_aryl_hydrocarbon","s":"ativo","d":"Aryl Hydrocarbon","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_aryl_hydrocarbon"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
