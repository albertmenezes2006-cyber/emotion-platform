#!/usr/bin/env python3
"""Protocolo sessão inicial"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sessao-inicial", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "sessao_inicial_protocolo", "status": "ativo",
                          "descricao": "Protocolo sessão inicial",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "sessao_inicial_protocolo",
                          "descricao": "Protocolo sessão inicial",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "sessao_inicial_protocolo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
