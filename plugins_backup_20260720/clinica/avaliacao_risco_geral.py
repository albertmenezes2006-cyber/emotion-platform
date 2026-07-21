#!/usr/bin/env python3
"""Avaliação de risco geral"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/risco-geral", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "avaliacao_risco_geral", "status": "ativo",
                          "descricao": "Avaliação de risco geral",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "avaliacao_risco_geral",
                          "descricao": "Avaliação de risco geral",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "avaliacao_risco_geral"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
