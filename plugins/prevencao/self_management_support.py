#!/usr/bin/env python3
"""Suporte ao autogerenciamento"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/autogestao", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "self_management_support", "status": "ativo",
                          "descricao": "Suporte ao autogerenciamento",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "self_management_support",
                          "descricao": "Suporte ao autogerenciamento",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "self_management_support"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
