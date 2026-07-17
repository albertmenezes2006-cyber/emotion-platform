#!/usr/bin/env python3
"""Neurodivergência no adulto"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/neurodiv-adulto", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "neurodivergente_adulto", "status": "ativo",
                          "descricao": "Neurodivergência no adulto",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "neurodivergente_adulto",
                          "descricao": "Neurodivergência no adulto",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "neurodivergente_adulto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
