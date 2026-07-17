from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/brow_lowerer", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_brow_lowerer","s":"ativo","d":"Brow Lowerer","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_brow_lowerer"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
