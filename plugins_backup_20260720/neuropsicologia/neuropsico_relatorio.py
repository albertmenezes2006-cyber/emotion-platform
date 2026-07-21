#!/usr/bin/env python3
"""Relatório neuropsicológico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/neuropsi-relatorio", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "neuropsico_relatorio", "status": "ativo",
                          "descricao": "Relatório neuropsicológico",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "neuropsico_relatorio",
                          "descricao": "Relatório neuropsicológico",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "neuropsico_relatorio"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
