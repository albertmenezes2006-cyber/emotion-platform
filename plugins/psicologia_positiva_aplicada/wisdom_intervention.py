from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/wisdom_intervention", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_wisdom_intervention","s":"ativo","d":"Wisdom Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_wisdom_intervention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
