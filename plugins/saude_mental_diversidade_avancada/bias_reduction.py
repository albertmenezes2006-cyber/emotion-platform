from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/bias_reduction", tags=["saude_mental_diversidade_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_di_bias_reduction","s":"ativo","d":"Bias Reduction","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_di_bias_reduction"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
