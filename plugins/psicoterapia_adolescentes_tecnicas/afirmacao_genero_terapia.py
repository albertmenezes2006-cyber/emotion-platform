from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/afirmacao_genero_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_afirmacao_genero_terap","s":"ativo","d":"Afirmacao Genero Terapia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_afirmacao_genero_terap"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
