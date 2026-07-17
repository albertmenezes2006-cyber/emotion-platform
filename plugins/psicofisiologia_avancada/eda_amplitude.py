from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/eda_amplitude", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_eda_amplitude","s":"ativo","d":"Eda Amplitude","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_eda_amplitude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
