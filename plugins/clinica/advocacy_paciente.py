#!/usr/bin/env python3
"""Advocacy pelo paciente"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/advocacy-pac", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "advocacy_paciente", "status": "ativo",
                          "descricao": "Advocacy pelo paciente",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "advocacy_paciente",
                          "descricao": "Advocacy pelo paciente",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "advocacy_paciente"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
