from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/ceremony_intervention", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_ceremony_intervention","s":"ativo","d":"Ceremony Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_ceremony_intervention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
