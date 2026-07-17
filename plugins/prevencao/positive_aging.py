#!/usr/bin/env python3
"""Envelhecimento positivo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/envelhecer-positivo", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "positive_aging", "status": "ativo",
                          "descricao": "Envelhecimento positivo",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "positive_aging",
                          "descricao": "Envelhecimento positivo",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "positive_aging"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
