from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacolog/ghrelin_mental", tags=["farmacologia_psiquiatrica_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"farmacologia_ps_ghrelin_mental","s":"ativo","d":"Ghrelin Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacologia_ps_ghrelin_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
