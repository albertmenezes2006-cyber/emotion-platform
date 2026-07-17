from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/legal_counseling_eap", tags=["saude_mental_trabalho_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_tr_legal_counseling_eap","s":"ativo","d":"Legal Counseling Eap","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_tr_legal_counseling_eap"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
