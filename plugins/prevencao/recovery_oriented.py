#!/usr/bin/env python3
"""Prática orientada à recuperação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/recovery", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "recovery_oriented", "status": "ativo",
                          "descricao": "Prática orientada à recuperação",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "recovery_oriented",
                          "descricao": "Prática orientada à recuperação",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "recovery_oriented"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
