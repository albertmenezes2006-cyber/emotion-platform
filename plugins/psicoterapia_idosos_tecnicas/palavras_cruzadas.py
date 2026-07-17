from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/palavras_cruzadas", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_palavras_cruzadas","s":"ativo","d":"Palavras Cruzadas","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_palavras_cruzadas"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
