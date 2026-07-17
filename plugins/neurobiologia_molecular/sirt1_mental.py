from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/sirt1_mental", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_sirt1_mental","s":"ativo","d":"Sirt1 Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_sirt1_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
