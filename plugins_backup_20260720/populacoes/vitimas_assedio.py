#!/usr/bin/env python3
"""Suporte a vítimas de assédio"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/assedio", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "vitimas_assedio", "status": "ativo",
                          "descricao": "Suporte a vítimas de assédio",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "vitimas_assedio",
                          "descricao": "Suporte a vítimas de assédio",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "vitimas_assedio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
