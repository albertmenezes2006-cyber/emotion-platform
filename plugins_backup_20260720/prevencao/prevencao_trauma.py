#!/usr/bin/env python3
"""Prevenção ao trauma"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prev-trauma", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "prevencao_trauma", "status": "ativo",
                          "descricao": "Prevenção ao trauma",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "prevencao_trauma",
                          "descricao": "Prevenção ao trauma",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "prevencao_trauma"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
