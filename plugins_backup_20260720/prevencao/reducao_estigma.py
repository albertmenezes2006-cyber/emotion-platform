#!/usr/bin/env python3
"""Redução do estigma em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/estigma", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "reducao_estigma", "status": "ativo",
                          "descricao": "Redução do estigma em saúde mental",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "reducao_estigma",
                          "descricao": "Redução do estigma em saúde mental",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "reducao_estigma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
