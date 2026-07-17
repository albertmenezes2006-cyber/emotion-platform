from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/mindfulness_intervention", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_mindfulness_interventi","s":"ativo","d":"Mindfulness Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_mindfulness_interventi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
