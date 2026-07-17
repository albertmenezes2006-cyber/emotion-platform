from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/sinal_clinico", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__sinal_clinico","s":"ativo","d":"Sinal Clinico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__sinal_clinico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
