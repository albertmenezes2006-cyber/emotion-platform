from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicoterap/imagem_corporal_terapia", tags=["psicoterapia_adolescentes_tecnicas"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicoterapia_ad_imagem_corporal_terapi","s":"ativo","d":"Imagem Corporal Terapia","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicoterapia_ad_imagem_corporal_terapi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
