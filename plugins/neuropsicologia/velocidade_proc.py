#!/usr/bin/env python3
"""Velocidade de processamento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/velocidade-proc", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "velocidade_proc", "status": "ativo",
                          "descricao": "Velocidade de processamento",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "velocidade_proc",
                          "descricao": "Velocidade de processamento",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "velocidade_proc"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
