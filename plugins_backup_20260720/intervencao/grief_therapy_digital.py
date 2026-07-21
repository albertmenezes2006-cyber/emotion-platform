#!/usr/bin/env python3
"""Terapia do luto digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/luto-terapia", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "grief_therapy_digital", "status": "ativo",
                          "descricao": "Terapia do luto digital",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "grief_therapy_digital",
                          "descricao": "Terapia do luto digital",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "grief_therapy_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
