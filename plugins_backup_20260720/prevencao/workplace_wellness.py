#!/usr/bin/env python3
"""Wellness no trabalho"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/trabalho-wellness", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "workplace_wellness", "status": "ativo",
                          "descricao": "Wellness no trabalho",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "workplace_wellness",
                          "descricao": "Wellness no trabalho",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "workplace_wellness"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
