#!/usr/bin/env python3
"""Movimento antimanicomial"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/antimanicomial", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "antimanicomial_info", "status": "ativo",
                          "descricao": "Movimento antimanicomial",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "antimanicomial_info",
                          "descricao": "Movimento antimanicomial",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "antimanicomial_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
