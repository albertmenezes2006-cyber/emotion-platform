from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/imagined_scenarios", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_imagined_scenarios","s":"ativo","d":"Imagined Scenarios","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_imagined_scenarios"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
