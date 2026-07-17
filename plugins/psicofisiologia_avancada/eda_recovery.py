from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/eda_recovery", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_eda_recovery","s":"ativo","d":"Eda Recovery","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_eda_recovery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
