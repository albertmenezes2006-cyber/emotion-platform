#!/usr/bin/env python3
"""Movimento de recovery"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/movimento-recovery", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "movement_recovery", "status": "ativo",
                          "descricao": "Movimento de recovery",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "movement_recovery",
                          "descricao": "Movimento de recovery",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "movement_recovery"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
