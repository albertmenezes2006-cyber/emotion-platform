from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/comorbidade2", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__comorbidade2","s":"ativo","d":"Comorbidade2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__comorbidade2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
