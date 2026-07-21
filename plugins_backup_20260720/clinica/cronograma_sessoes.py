#!/usr/bin/env python3
"""Cronograma de sessões terapêuticas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cronograma", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cronograma_sessoes", "status": "ativo",
                          "descricao": "Cronograma de sessões terapêuticas",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cronograma_sessoes",
                          "descricao": "Cronograma de sessões terapêuticas",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cronograma_sessoes"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
