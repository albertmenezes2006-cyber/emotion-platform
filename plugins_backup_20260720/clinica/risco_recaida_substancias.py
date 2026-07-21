#!/usr/bin/env python3
"""Risco de recaída substâncias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/risco-recaida", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "risco_recaida_substancias", "status": "ativo",
                          "descricao": "Risco de recaída substâncias",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "risco_recaida_substancias",
                          "descricao": "Risco de recaída substâncias",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "risco_recaida_substancias"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
