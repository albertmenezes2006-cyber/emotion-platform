#!/usr/bin/env python3
"""Sobreviventes de UTI"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/uti-sobrevivente", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "uti_sobreviventes", "status": "ativo",
                          "descricao": "Sobreviventes de UTI",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "uti_sobreviventes",
                          "descricao": "Sobreviventes de UTI",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "uti_sobreviventes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
