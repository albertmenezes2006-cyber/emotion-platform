#!/usr/bin/env python3
"""LSAS Liebowitz Social Anxiety"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lsas", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lsas_liebowitz", "status": "ativo",
                          "descricao": "LSAS Liebowitz Social Anxiety",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "lsas_liebowitz",
                          "descricao": "LSAS Liebowitz Social Anxiety",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lsas_liebowitz"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
