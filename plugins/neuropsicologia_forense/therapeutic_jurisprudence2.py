from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/therapeutic_jurisprudence", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_therapeutic_jurisprude","s":"ativo","d":"Therapeutic Jurisprudence2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_therapeutic_jurisprude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
