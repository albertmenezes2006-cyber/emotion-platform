from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/pupil_light_reflex", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_pupil_light_reflex","s":"ativo","d":"Pupil Light Reflex","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_pupil_light_reflex"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
