from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/smoking_cessation2", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_smoking_cessation2","s":"ativo","d":"Smoking Cessation2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_smoking_cessation2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
