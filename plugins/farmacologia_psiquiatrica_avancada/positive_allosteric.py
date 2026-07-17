from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacolog/positive_allosteric", tags=["farmacologia_psiquiatrica_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"farmacologia_ps_positive_allosteric","s":"ativo","d":"Positive Allosteric","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacologia_ps_positive_allosteric"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
