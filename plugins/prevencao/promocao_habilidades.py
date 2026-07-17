#!/usr/bin/env python3
"""Promoção de habilidades sociais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/prom-habilidades", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "promocao_habilidades", "status": "ativo",
                          "descricao": "Promoção de habilidades sociais",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "promocao_habilidades",
                          "descricao": "Promoção de habilidades sociais",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "promocao_habilidades"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
