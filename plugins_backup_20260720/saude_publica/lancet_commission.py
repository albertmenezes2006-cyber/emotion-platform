#!/usr/bin/env python3
"""Lancet Commission Saúde Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lancet-mental", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lancet_commission", "status": "ativo",
                          "descricao": "Lancet Commission Saúde Mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "lancet_commission",
                          "descricao": "Lancet Commission Saúde Mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lancet_commission"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
