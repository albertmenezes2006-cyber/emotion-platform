#!/usr/bin/env python3
"""Flashback protocolo de manejo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/flashback", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "flashback_protocolo", "status": "ativo",
                          "descricao": "Flashback protocolo de manejo",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "flashback_protocolo",
                          "descricao": "Flashback protocolo de manejo",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "flashback_protocolo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
