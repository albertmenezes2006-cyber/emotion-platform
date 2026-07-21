#!/usr/bin/env python3
"""Psicoeducação TEA"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psicoed-tea", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psicoeducacao_tea", "status": "ativo",
                          "descricao": "Psicoeducação TEA",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psicoeducacao_tea",
                          "descricao": "Psicoeducação TEA",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psicoeducacao_tea"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
