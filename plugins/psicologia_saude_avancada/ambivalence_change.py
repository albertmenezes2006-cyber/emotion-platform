from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/ambivalence_change", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_ambivalence_change","s":"ativo","d":"Ambivalence Change","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_ambivalence_change"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
