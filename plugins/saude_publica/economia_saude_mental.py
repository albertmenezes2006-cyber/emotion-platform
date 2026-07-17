#!/usr/bin/env python3
"""Economia da saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/economia-sm", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "economia_saude_mental", "status": "ativo",
                          "descricao": "Economia da saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "economia_saude_mental",
                          "descricao": "Economia da saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "economia_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
