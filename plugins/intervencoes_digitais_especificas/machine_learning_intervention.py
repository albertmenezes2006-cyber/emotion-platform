from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/intervenco/machine_learning_interven", tags=["intervencoes_digitais_especificas"])
@router.get("")
async def i():
    return JSONResponse({"p":"intervencoes_di_machine_learning_inter","s":"ativo","d":"Machine Learning Intervention","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "intervencoes_di_machine_learning_inter"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
