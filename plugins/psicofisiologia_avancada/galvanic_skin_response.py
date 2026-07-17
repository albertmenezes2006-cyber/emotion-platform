from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/galvanic_skin_response", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_galvanic_skin_response","s":"ativo","d":"Galvanic Skin Response","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_galvanic_skin_response"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
