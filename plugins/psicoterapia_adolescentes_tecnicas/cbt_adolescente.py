from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/cbt_adolescente", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_cbt_adolescente","s":"ativo","d":"Cbt Adolescente","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_cbt_adolescente"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
