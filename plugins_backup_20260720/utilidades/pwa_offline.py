#!/usr/bin/env python3
"""Pagina offline para PWA"""
from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from plugins.plugin_base import PluginBase
from pathlib import Path

router = APIRouter(tags=["PWA"])

@router.get("/offline", response_class=HTMLResponse)
async def offline():
    p = Path("templates/offline.html")
    return HTMLResponse(p.read_text() if p.exists() else "<h1>Offline</h1>")

class OfflinePlugin(PluginBase):
    name = "pwa_offline"
    def setup(self, app): app.include_router(router)
plugin = OfflinePlugin()
