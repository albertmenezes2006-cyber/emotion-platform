from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/serine_threonine_kinase", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_serine_threonine_kinas","s":"ativo","d":"Serine Threonine Kinase","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_serine_threonine_kinas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
