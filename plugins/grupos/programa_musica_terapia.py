#!/usr/bin/env python3
"""Programa musicoterapia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/musica-prog", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_musica_terapia", "status": "ativo",
                          "descricao": "Programa musicoterapia",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_musica_terapia",
                          "descricao": "Programa musicoterapia",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_musica_terapia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
