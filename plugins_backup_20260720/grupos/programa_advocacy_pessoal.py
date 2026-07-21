#!/usr/bin/env python3
"""Programa advocacy pessoal"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/advocacy-pessoal", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_advocacy_pessoal", "status": "ativo",
                          "descricao": "Programa advocacy pessoal",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_advocacy_pessoal",
                          "descricao": "Programa advocacy pessoal",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_advocacy_pessoal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
