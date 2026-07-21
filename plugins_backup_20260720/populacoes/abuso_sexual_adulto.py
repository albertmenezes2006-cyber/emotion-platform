#!/usr/bin/env python3
"""Suporte a sobreviventes de abuso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/abuso-sexual", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "abuso_sexual_adulto", "status": "ativo",
                          "descricao": "Suporte a sobreviventes de abuso",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "abuso_sexual_adulto",
                          "descricao": "Suporte a sobreviventes de abuso",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "abuso_sexual_adulto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
