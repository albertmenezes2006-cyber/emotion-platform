#!/usr/bin/env python3
"""CREPOP práticas psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/crepop", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "crepop_psico", "status": "ativo",
                          "descricao": "CREPOP práticas psicologia",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "crepop_psico",
                          "descricao": "CREPOP práticas psicologia",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "crepop_psico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
