from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/lip_corner_pull", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_lip_corner_pull","s":"ativo","d":"Lip Corner Pull","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_lip_corner_pull"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
