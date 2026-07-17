from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/suggestibilidade_adulto", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_suggestibilidade_adult","s":"ativo","d":"Suggestibilidade Adulto","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_suggestibilidade_adult"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
