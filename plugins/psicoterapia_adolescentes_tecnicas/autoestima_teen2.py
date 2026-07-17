from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/autoestima_teen2", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_autoestima_teen2","s":"ativo","d":"Autoestima Teen2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_autoestima_teen2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
