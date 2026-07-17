from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/epistemolo/linguagem_sem_pensamento", tags=["epistemologia_psicologia"])
@router.get("")
async def i():
    return JSONResponse({"p":"epistemologia_p_linguagem_sem_pensamen","s":"ativo","d":"Linguagem Sem Pensamento","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "epistemologia_p_linguagem_sem_pensamen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
