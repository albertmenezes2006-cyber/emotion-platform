from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/masked_hypertension", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_masked_hypertension","s":"ativo","d":"Masked Hypertension","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_masked_hypertension"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
