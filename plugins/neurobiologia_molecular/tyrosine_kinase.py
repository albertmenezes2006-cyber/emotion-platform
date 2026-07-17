from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/tyrosine_kinase", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_tyrosine_kinase","s":"ativo","d":"Tyrosine Kinase","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_tyrosine_kinase"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
