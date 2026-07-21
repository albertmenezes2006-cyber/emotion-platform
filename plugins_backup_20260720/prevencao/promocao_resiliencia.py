#!/usr/bin/env python3
"""Promoção da resiliência"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prom-resiliencia", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "promocao_resiliencia", "status": "ativo",
                          "descricao": "Promoção da resiliência",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "promocao_resiliencia",
                          "descricao": "Promoção da resiliência",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "promocao_resiliencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
