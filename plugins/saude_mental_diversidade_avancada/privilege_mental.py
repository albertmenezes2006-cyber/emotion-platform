from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/privilege_mental", tags=["saude_mental_diversidade_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_di_privilege_mental","s":"ativo","d":"Privilege Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_di_privilege_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
