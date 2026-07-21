#!/usr/bin/env python3
"""Promoção do bem-estar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prom-bem-estar", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "promocao_bemestar", "status": "ativo",
                          "descricao": "Promoção do bem-estar",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "promocao_bemestar",
                          "descricao": "Promoção do bem-estar",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "promocao_bemestar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
