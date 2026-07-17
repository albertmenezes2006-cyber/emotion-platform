from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurobiolo/glucocorticoid_receptor", tags=["neurobiologia_molecular"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurobiologia_m_glucocorticoid_recepto","s":"ativo","d":"Glucocorticoid Receptor","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurobiologia_m_glucocorticoid_recepto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
