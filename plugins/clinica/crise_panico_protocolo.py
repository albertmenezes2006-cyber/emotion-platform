#!/usr/bin/env python3
"""Protocolo crise de pânico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/panico-crise", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "crise_panico_protocolo", "status": "ativo",
                          "descricao": "Protocolo crise de pânico",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "crise_panico_protocolo",
                          "descricao": "Protocolo crise de pânico",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "crise_panico_protocolo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
