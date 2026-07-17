from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/job_redesign", tags=["saude_mental_trabalho_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_tr_job_redesign","s":"ativo","d":"Job Redesign","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_tr_job_redesign"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
