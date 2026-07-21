#!/usr/bin/env python3
"""Entrevista motivacional digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/motivacional", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "motivational_interv", "status": "ativo",
                          "descricao": "Entrevista motivacional digital",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "motivational_interv",
                          "descricao": "Entrevista motivacional digital",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "motivational_interv"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
