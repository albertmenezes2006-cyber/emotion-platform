from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/pensamento_sem_linguagem", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_pensamento_sem_linguag","s":"ativo","d":"Pensamento Sem Linguagem","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_pensamento_sem_linguag"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
