from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/climate_fairness", tags=["saude_mental_trabalho_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_tr_climate_fairness","s":"ativo","d":"Climate Fairness","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_tr_climate_fairness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
