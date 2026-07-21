#!/usr/bin/env python3
"""CAPS tipos e serviços"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/caps-tipos", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "caps_tipos_servicos", "status": "ativo",
                          "descricao": "CAPS tipos e serviços",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "caps_tipos_servicos",
                          "descricao": "CAPS tipos e serviços",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "caps_tipos_servicos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
