#!/usr/bin/env python3
"""Promoção da autoestima"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prom-autoestima", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "promocao_autoestima", "status": "ativo",
                          "descricao": "Promoção da autoestima",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "promocao_autoestima",
                          "descricao": "Promoção da autoestima",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "promocao_autoestima"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
