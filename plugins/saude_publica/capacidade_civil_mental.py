#!/usr/bin/env python3
"""Capacidade civil e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/capacidade-civil", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "capacidade_civil_mental", "status": "ativo",
                          "descricao": "Capacidade civil e saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "capacidade_civil_mental",
                          "descricao": "Capacidade civil e saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "capacidade_civil_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
