from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/sd2_poincare", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_sd2_poincare","s":"ativo","d":"Sd2 Poincare","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_sd2_poincare"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
