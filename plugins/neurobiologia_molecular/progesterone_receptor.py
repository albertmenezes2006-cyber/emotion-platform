from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/progesterone_receptor", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_progesterone_receptor","s":"ativo","d":"Progesterone Receptor","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_progesterone_receptor"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
