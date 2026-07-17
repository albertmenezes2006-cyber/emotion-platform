from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/helping_others", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_helping_others","s":"ativo","d":"Helping Others","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_helping_others"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
