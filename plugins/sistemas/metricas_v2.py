from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, sys
router = APIRouter(prefix="/api/v1/metricas", tags=["Metricas"])
_ini = datetime.utcnow(); _req = 0
@router.get("")
async def metricas():
    global _req; _req+=1; up=(datetime.utcnow()-_ini).total_seconds()
    return JSONResponse({"uptime_s":round(up),"uptime_h":round(up/3600,2),"requests":_req,"python":sys.version.split()[0],"ambiente":os.getenv("RENDER","local"),"ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "metricas_v2"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
