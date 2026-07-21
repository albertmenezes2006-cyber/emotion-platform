#!/usr/bin/env python3
"""SafeTALK treinamento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/safetalk", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "safeTALK_training", "status": "ativo",
                          "descricao": "SafeTALK treinamento",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "safeTALK_training",
                          "descricao": "SafeTALK treinamento",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "safeTALK_training"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
