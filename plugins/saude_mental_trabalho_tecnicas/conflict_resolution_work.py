from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_ment/conflict_resolution_work", tags=["saude_mental_trabalho_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"saude_mental_tr_conflict_resolution_wo","s":"ativo","d":"Conflict Resolution Work","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_tr_conflict_resolution_wo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
