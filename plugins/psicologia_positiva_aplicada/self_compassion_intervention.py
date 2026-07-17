from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/self_compassion_intervent", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_self_compassion_interv","s":"ativo","d":"Self Compassion Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_self_compassion_interv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
