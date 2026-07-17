from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/farmacolog/gdnf_gfralpha", tags=["farmacologia_psiquiatrica_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"farmacologia_ps_gdnf_gfralpha","s":"ativo","d":"Gdnf Gfralpha","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "farmacologia_ps_gdnf_gfralpha"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
