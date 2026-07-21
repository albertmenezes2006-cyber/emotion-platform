#!/usr/bin/env python3
"""Protocolo sessão emergência"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sessao-emergencia", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sessao_emergencia_protocol", "status": "ativo",
                          "descricao": "Protocolo sessão emergência",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "sessao_emergencia_protocol",
                          "descricao": "Protocolo sessão emergência",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sessao_emergencia_protocol"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
