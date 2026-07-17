from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/migracao_adolescente_tera", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_migracao_adolescente_t","s":"ativo","d":"Migracao Adolescente Terapia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_migracao_adolescente_t"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
