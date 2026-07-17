from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/psicopatologia_psicodinam", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__psicopatologia_psicodi","s":"ativo","d":"Psicopatologia Psicodinamica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__psicopatologia_psicodi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
