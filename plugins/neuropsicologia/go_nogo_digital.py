#!/usr/bin/env python3
"""Go/No-Go controle inibitório"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/go-nogo", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "go_nogo_digital", "status": "ativo",
                          "descricao": "Go/No-Go controle inibitório",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "go_nogo_digital",
                          "descricao": "Go/No-Go controle inibitório",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "go_nogo_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
