from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/racial_capitalism", tags=["saude_mental_diversidade_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_di_racial_capitalism","s":"ativo","d":"Racial Capitalism","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_di_racial_capitalism"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
