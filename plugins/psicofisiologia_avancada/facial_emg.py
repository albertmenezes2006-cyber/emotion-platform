from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicofisio/facial_emg", tags=["psicofisiologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicofisiologia_facial_emg","s":"ativo","d":"Facial Emg","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicofisiologia_facial_emg"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
