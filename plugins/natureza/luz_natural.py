#!/usr/bin/env python3
"""Exposição à luz natural"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/luz", tags=["Natureza"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "luz_natural", "status": "ativo",
                          "descricao": "Exposição à luz natural",
                          "versao": "1.0.0",
                          "categoria": "natureza",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "luz_natural"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
