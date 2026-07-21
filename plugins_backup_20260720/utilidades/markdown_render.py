#!/usr/bin/env python3
"""Renderizador de Markdown"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/markdown", tags=["markdown_render"])

@router.get("")
async def info():
    return JSONResponse({"nome": "markdown_render", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "markdown_render"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
