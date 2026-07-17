#!/usr/bin/env python3
"""Telepsiquiatria no SUS"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tele-sus", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "telepsiquiatria_sus", "status": "ativo",
                          "descricao": "Telepsiquiatria no SUS",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "telepsiquiatria_sus",
                          "descricao": "Telepsiquiatria no SUS",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "telepsiquiatria_sus"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
