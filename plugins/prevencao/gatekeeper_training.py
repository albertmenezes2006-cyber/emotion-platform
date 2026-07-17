#!/usr/bin/env python3
"""Treinamento de guardiões vida"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/gatekeeper", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "gatekeeper_training", "status": "ativo",
                          "descricao": "Treinamento de guardiões vida",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "gatekeeper_training",
                          "descricao": "Treinamento de guardiões vida",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "gatekeeper_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
