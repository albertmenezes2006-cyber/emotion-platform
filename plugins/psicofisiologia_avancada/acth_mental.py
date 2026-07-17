from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/acth_mental", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_acth_mental","s":"ativo","d":"Acth Mental","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_acth_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
