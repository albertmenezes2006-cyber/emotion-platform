#!/usr/bin/env python3
"""Determinantes sociais da saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/determinantes", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "social_determinants", "status": "ativo",
                          "descricao": "Determinantes sociais da saúde",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "social_determinants",
                          "descricao": "Determinantes sociais da saúde",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "social_determinants"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
