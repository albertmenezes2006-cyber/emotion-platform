#!/usr/bin/env python3
"""Protocolo de follow-up"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/follow-up", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "follow_up_protocolo", "status": "ativo",
                          "descricao": "Protocolo de follow-up",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "follow_up_protocolo",
                          "descricao": "Protocolo de follow-up",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "follow_up_protocolo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
