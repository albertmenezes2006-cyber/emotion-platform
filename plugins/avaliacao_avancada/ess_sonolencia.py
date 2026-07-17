#!/usr/bin/env python3
"""Epworth Sleepiness Scale"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ess", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ess_sonolencia", "status": "ativo",
                          "descricao": "Epworth Sleepiness Scale",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ess_sonolencia",
                          "descricao": "Epworth Sleepiness Scale",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ess_sonolencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
