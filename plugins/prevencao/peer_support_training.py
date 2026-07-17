#!/usr/bin/env python3
"""Treinamento de pares"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pares-train", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "peer_support_training", "status": "ativo",
                          "descricao": "Treinamento de pares",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "peer_support_training",
                          "descricao": "Treinamento de pares",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "peer_support_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
