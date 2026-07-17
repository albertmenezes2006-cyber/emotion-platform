from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/contemplacao_idoso", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_contemplacao_idoso","s":"ativo","d":"Contemplacao Idoso","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_contemplacao_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
