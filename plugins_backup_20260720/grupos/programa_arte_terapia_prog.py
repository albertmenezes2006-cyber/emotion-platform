#!/usr/bin/env python3
"""Programa arteterapia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/arte-prog", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_arte_terapia_prog", "status": "ativo",
                          "descricao": "Programa arteterapia",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_arte_terapia_prog",
                          "descricao": "Programa arteterapia",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_arte_terapia_prog"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
