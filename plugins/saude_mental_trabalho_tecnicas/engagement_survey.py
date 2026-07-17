from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/engagement_survey", tags=["saude_mental_trabalho_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_tr_engagement_survey","s":"ativo","d":"Engagement Survey","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_tr_engagement_survey"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
