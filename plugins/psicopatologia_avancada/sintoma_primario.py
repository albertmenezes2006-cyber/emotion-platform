from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/sintoma_primario", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__sintoma_primario","s":"ativo","d":"Sintoma Primario","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__sintoma_primario"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
