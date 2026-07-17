from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/partial_hospitalization", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_partial_hospitalizatio","s":"ativo","d":"Partial Hospitalization","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_partial_hospitalizatio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
