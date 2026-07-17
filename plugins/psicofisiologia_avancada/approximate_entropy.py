from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/approximate_entropy", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_approximate_entropy","s":"ativo","d":"Approximate Entropy","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_approximate_entropy"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
