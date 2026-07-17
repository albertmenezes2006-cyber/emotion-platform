#!/usr/bin/env python3
"""Automutilação manejo clínico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/automut-manejo", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "automutilacao_manejo", "status": "ativo",
                          "descricao": "Automutilação manejo clínico",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "automutilacao_manejo",
                          "descricao": "Automutilação manejo clínico",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "automutilacao_manejo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
