from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/wayfinding", tags=["psicologia_ambiental_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_ambi_wayfinding","s":"ativo","d":"Wayfinding","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_ambi_wayfinding"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
