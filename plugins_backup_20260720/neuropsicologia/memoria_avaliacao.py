#!/usr/bin/env python3
"""Memória avaliação digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/memoria-aval", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "memoria_avaliacao", "status": "ativo",
                          "descricao": "Memória avaliação digital",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "memoria_avaliacao",
                          "descricao": "Memória avaliação digital",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "memoria_avaliacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
