from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/instrumentalismo", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_instrumentalismo","s":"ativo","d":"Instrumentalismo","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_instrumentalismo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
