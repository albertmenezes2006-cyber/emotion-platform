from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/systolic_bp", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_systolic_bp","s":"ativo","d":"Systolic Bp","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_systolic_bp"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
