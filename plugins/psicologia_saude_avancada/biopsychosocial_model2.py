from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/biopsychosocial_model2", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_biopsychosocial_model2","s":"ativo","d":"Biopsychosocial Model2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_biopsychosocial_model2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
