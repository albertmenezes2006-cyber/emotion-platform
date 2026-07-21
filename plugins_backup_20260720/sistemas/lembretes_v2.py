from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase

router = APIRouter(prefix="/api/v1/lembretes-sys", tags=["Lembretes Sys"])

@router.get("")
async def info():
    return JSONResponse({"status": "ok", "msg": "Use /api/v1/lembretes"})

class Plugin(PluginBase):
    name = "lembretes_sys_redirect"
    def setup(self, app):
        app.include_router(router)

plugin = Plugin()
