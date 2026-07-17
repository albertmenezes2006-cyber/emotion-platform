from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/rivers_mental", tags=["psicologia_ambiental_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_ambi_rivers_mental","s":"ativo","d":"Rivers Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_ambi_rivers_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
