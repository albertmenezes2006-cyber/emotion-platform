from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia/exercise_intervention2", tags=["psicologia_positiva_aplicada"])
@router.get("")
async def i():
    return JSONResponse({"p":"psicologia_posi_exercise_intervention2","s":"ativo","d":"Exercise Intervention2","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_posi_exercise_intervention2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
