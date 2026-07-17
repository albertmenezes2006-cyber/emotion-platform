#!/usr/bin/env python3
"""Linguagem avaliação neuropsico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/linguagem-aval", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "linguagem_avaliacao", "status": "ativo",
                          "descricao": "Linguagem avaliação neuropsico",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "linguagem_avaliacao",
                          "descricao": "Linguagem avaliação neuropsico",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "linguagem_avaliacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
