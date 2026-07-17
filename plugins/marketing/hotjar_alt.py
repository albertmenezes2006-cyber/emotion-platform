#!/usr/bin/env python3
"""Heatmap alternativo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/heatmap", tags=["hotjar_alt"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "hotjar_alt", "status": "ativo",
                          "descricao": "Heatmap alternativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "hotjar_alt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
