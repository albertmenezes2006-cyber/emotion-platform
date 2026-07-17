from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/dexamethasone_test", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_dexamethasone_test","s":"ativo","d":"Dexamethasone Test","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_dexamethasone_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
