#!/usr/bin/env python3
"""Avaliação de intoxicação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/intoxicacao-aval", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "intoxicacao_avaliacao", "status": "ativo",
                          "descricao": "Avaliação de intoxicação",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "intoxicacao_avaliacao",
                          "descricao": "Avaliação de intoxicação",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "intoxicacao_avaliacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
