from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/qualidade_vida_psico", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__qualidade_vida_psico","s":"ativo","d":"Qualidade Vida Psico","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__qualidade_vida_psico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
