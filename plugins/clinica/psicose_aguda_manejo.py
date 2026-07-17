#!/usr/bin/env python3
"""Psicose aguda manejo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/psicose-aguda", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "psicose_aguda_manejo", "status": "ativo",
                          "descricao": "Psicose aguda manejo",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "psicose_aguda_manejo",
                          "descricao": "Psicose aguda manejo",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "psicose_aguda_manejo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
