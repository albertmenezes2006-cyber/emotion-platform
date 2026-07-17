from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/concordance_medical", tags=["psicologia_saude_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_saud_concordance_medical","s":"ativo","d":"Concordance Medical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_saud_concordance_medical"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
