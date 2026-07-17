from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/obesity_psychology", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_obesity_psychology","s":"ativo","d":"Obesity Psychology","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_obesity_psychology"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
