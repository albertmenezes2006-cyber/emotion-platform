from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/social_media_intervention", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_social_media_intervent","s":"ativo","d":"Social Media Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_social_media_intervent"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
