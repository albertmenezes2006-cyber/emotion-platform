from fastapi import APIRouter
from fastapi.responses import FileResponse, JSONResponse
from plugins.plugin_base import PluginBase
import os

router = APIRouter(tags=["PWA"])

@router.get("/.well-known/assetlinks.json")
async def assetlinks():
    path = "static/.well-known/assetlinks.json"
    if os.path.exists(path):
        return FileResponse(path, media_type="application/json")
    return JSONResponse([])

@router.get("/static/manifest.json")
async def manifest():
    path = "static/manifest.json"
    if os.path.exists(path):
        return FileResponse(path, media_type="application/json")
    return JSONResponse({})

class Plugin(PluginBase):
    name = "pwa_assetlinks"
    def setup(self, app):
        app.include_router(router)

plugin = Plugin()
