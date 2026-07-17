from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/parks_mental", tags=["psicologia_ambiental_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_ambi_parks_mental","s":"ativo","d":"Parks Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_ambi_parks_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
