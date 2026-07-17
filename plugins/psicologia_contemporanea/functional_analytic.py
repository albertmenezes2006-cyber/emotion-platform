from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/functional_analytic", tags=["psicologia_contemporanea"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_cont_functional_analytic","s":"ativo","d":"Functional Analytic","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_cont_functional_analytic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
