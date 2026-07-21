#!/usr/bin/env python3
"""Programa dança-movimento terapia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/danca-terapia", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_dança_terapia", "status": "ativo",
                          "descricao": "Programa dança-movimento terapia",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_dança_terapia",
                          "descricao": "Programa dança-movimento terapia",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_dança_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
