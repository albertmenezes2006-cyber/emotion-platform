#!/usr/bin/env python3
"""LEC-5 Lista de eventos traumáticos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lec5", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lec5_eventos", "status": "ativo",
                          "descricao": "LEC-5 Lista de eventos traumáticos",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "lec5_eventos",
                          "descricao": "LEC-5 Lista de eventos traumáticos",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lec5_eventos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
