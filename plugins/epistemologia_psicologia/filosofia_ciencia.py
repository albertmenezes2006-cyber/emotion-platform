from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/filosofia_ciencia", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_filosofia_ciencia","s":"ativo","d":"Filosofia Ciencia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_filosofia_ciencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
