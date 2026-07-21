#!/usr/bin/env python3
"""Pesadelos recorrentes manejo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pesadelo", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "pesadelo_recorrente", "status": "ativo",
                          "descricao": "Pesadelos recorrentes manejo",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "pesadelo_recorrente",
                          "descricao": "Pesadelos recorrentes manejo",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "pesadelo_recorrente"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
