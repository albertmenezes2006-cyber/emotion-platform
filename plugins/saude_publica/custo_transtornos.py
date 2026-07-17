#!/usr/bin/env python3
"""Custo econômico transtornos mentais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/custo-transtornos", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "custo_transtornos", "status": "ativo",
                          "descricao": "Custo econômico transtornos mentais",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "custo_transtornos",
                          "descricao": "Custo econômico transtornos mentais",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "custo_transtornos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
