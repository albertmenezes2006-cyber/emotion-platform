from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/lf_hf_ratio", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_lf_hf_ratio","s":"ativo","d":"Lf Hf Ratio","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_lf_hf_ratio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
