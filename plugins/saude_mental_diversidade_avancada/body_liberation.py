from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/body_liberation", tags=["saude_mental_diversidade_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_di_body_liberation","s":"ativo","d":"Body Liberation","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_di_body_liberation"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
