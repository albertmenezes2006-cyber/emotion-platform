from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/atividade_fisica_idoso3", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_atividade_fisica_idoso","s":"ativo","d":"Atividade Fisica Idoso3","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_atividade_fisica_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
