from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/caminhada_idoso", tags=["psicoterapia_idosos_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_id_caminhada_idoso","s":"ativo","d":"Caminhada Idoso","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_id_caminhada_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
