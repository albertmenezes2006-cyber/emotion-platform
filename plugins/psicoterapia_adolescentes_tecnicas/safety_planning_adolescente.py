from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/safety_planning_adolescen", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_safety_planning_adoles","s":"ativo","d":"Safety Planning Adolescente","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_safety_planning_adoles"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
