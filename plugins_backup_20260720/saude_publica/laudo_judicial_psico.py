#!/usr/bin/env python3
"""Laudo psicológico judicial"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/laudo-judicial", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "laudo_judicial_psico", "status": "ativo",
                          "descricao": "Laudo psicológico judicial",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "laudo_judicial_psico",
                          "descricao": "Laudo psicológico judicial",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "laudo_judicial_psico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
