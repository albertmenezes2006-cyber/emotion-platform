from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neuropsico/testemunho_especialista", tags=["neuropsicologia_forense"])
@router.get("")
async def i():
    return JSONResponse({"p":"neuropsicologia_testemunho_especialist","s":"ativo","d":"Testemunho Especialista","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neuropsicologia_testemunho_especialist"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
