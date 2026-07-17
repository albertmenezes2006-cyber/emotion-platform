#!/usr/bin/env python3
"""ASRS TDAH adulto OMS"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/asrs", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "asrs_tdah_adulto", "status": "ativo",
                          "descricao": "ASRS TDAH adulto OMS",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "asrs_tdah_adulto",
                          "descricao": "ASRS TDAH adulto OMS",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "asrs_tdah_adulto"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
