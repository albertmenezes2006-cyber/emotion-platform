from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/neurocienc/boundary_cells", tags=["neurociencia_computacional"])
@router.get("")
async def i():
    return JSONResponse({"p":"neurociencia_co_boundary_cells","s":"ativo","d":"Boundary Cells","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "neurociencia_co_boundary_cells"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
