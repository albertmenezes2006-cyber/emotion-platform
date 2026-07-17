from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/entrevista_motivacional_t", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_entrevista_motivaciona","s":"ativo","d":"Entrevista Motivacional Teen","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_entrevista_motivaciona"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
