from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/sabedoria_transmissao", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_sabedoria_transmissao","s":"ativo","d":"Sabedoria Transmissao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_sabedoria_transmissao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
