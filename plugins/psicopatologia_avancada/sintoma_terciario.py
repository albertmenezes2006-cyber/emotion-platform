from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/sintoma_terciario", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__sintoma_terciario","s":"ativo","d":"Sintoma Terciario","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__sintoma_terciario"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
