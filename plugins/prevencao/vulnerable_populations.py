#!/usr/bin/env python3
"""Populações vulneráveis"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/vulneraveis", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "vulnerable_populations", "status": "ativo",
                          "descricao": "Populações vulneráveis",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "vulnerable_populations",
                          "descricao": "Populações vulneráveis",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "vulnerable_populations"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
