#!/usr/bin/env python3
"""Poeterapia digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/poesia", tags=["Arte Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "poesia_terapia", "status": "ativo",
                          "descricao": "Poeterapia digital",
                          "versao": "1.0.0",
                          "categoria": "arte_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "poesia_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
