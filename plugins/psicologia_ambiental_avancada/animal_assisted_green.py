from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/animal_assisted_green", tags=["psicologia_ambiental_avancada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_ambi_animal_assisted_green","s":"ativo","d":"Animal Assisted Green","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_ambi_animal_assisted_green"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
