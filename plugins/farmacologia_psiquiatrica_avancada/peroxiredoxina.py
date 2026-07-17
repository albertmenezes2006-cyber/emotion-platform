from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacolog/peroxiredoxina", tags=["farmacologia_psiquiatrica_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"farmacologia_ps_peroxiredoxina","s":"ativo","d":"Peroxiredoxina","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacologia_ps_peroxiredoxina"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
