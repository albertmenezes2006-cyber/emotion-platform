#!/usr/bin/env python3
"""Avaliação pericial psicológica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pericial-psico", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "avaliacao_pericial_psico", "status": "ativo",
                          "descricao": "Avaliação pericial psicológica",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "avaliacao_pericial_psico",
                          "descricao": "Avaliação pericial psicológica",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "avaliacao_pericial_psico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
