from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/skin_conductance", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_skin_conductance","s":"ativo","d":"Skin Conductance","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_skin_conductance"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
