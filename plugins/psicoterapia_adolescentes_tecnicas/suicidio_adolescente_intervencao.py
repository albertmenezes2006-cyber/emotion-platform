from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/suicidio_adolescente_inte", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_suicidio_adolescente_i","s":"ativo","d":"Suicidio Adolescente Intervencao","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_suicidio_adolescente_i"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
