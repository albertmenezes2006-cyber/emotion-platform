#!/usr/bin/env python3
"""Psicoeducação esquizofrenia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psicoed-esq", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psicoeducacao_esquizo", "status": "ativo",
                          "descricao": "Psicoeducação esquizofrenia",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psicoeducacao_esquizo",
                          "descricao": "Psicoeducação esquizofrenia",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psicoeducacao_esquizo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
