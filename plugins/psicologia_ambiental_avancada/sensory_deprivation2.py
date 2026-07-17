from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/sensory_deprivation2", tags=["psicologia_ambiental_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_ambi_sensory_deprivation2","s":"ativo","d":"Sensory Deprivation2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_ambi_sensory_deprivation2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
