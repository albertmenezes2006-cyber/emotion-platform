#!/usr/bin/env python3
"""Equidade em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/equidade", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "health_equity", "status": "ativo",
                          "descricao": "Equidade em saúde mental",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "health_equity",
                          "descricao": "Equidade em saúde mental",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "health_equity"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
