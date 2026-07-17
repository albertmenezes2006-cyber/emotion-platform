from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicopatol/sindrome_clinica", tags=["psicopatologia_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicopatologia__sindrome_clinica","s":"ativo","d":"Sindrome Clinica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicopatologia__sindrome_clinica"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
