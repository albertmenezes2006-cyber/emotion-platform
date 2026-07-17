from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/eda_frequency", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_eda_frequency","s":"ativo","d":"Eda Frequency","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_eda_frequency"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
