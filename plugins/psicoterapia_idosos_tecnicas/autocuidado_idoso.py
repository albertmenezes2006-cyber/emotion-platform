from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/autocuidado_idoso", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_autocuidado_idoso","s":"ativo","d":"Autocuidado Idoso","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_autocuidado_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
