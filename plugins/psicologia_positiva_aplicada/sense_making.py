from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/sense_making", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_sense_making","s":"ativo","d":"Sense Making","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_sense_making"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
