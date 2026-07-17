from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/pensamento_informal", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_pensamento_informal","s":"ativo","d":"Pensamento Informal","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_pensamento_informal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
