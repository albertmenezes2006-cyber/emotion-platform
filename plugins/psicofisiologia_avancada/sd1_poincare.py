from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/sd1_poincare", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_sd1_poincare","s":"ativo","d":"Sd1 Poincare","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_sd1_poincare"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
