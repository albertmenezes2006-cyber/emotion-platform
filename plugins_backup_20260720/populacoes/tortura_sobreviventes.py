#!/usr/bin/env python3
"""Suporte a sobreviventes de tortura"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tortura", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "tortura_sobreviventes", "status": "ativo",
                          "descricao": "Suporte a sobreviventes de tortura",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "tortura_sobreviventes",
                          "descricao": "Suporte a sobreviventes de tortura",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "tortura_sobreviventes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
