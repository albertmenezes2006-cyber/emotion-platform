#!/usr/bin/env python3
"""Autonomia do paciente"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/autonomia", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "autonomia_paciente", "status": "ativo",
                          "descricao": "Autonomia do paciente",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "autonomia_paciente",
                          "descricao": "Autonomia do paciente",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "autonomia_paciente"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
