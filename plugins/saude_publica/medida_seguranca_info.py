#!/usr/bin/env python3
"""Medida de segurança psiquiátrica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/medida-seguranca", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "medida_seguranca_info", "status": "ativo",
                          "descricao": "Medida de segurança psiquiátrica",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "medida_seguranca_info",
                          "descricao": "Medida de segurança psiquiátrica",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "medida_seguranca_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
