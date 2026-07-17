from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/nutrition_intervention2", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_nutrition_intervention","s":"ativo","d":"Nutrition Intervention2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_nutrition_intervention"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
