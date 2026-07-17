#!/usr/bin/env python3
"""Psicoeducação ansiedade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psicoed-ans", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psicoeducacao_ansiedade", "status": "ativo",
                          "descricao": "Psicoeducação ansiedade",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psicoeducacao_ansiedade",
                          "descricao": "Psicoeducação ansiedade",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psicoeducacao_ansiedade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
