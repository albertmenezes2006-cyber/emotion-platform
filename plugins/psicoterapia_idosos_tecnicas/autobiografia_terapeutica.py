from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/autobiografia_terapeutica", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_autobiografia_terapeut","s":"ativo","d":"Autobiografia Terapeutica","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_autobiografia_terapeut"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
