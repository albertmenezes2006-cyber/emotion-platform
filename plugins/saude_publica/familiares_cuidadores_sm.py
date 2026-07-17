#!/usr/bin/env python3
"""Familiares em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/familiares-sm", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "familiares_cuidadores_sm", "status": "ativo",
                          "descricao": "Familiares em saúde mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "familiares_cuidadores_sm",
                          "descricao": "Familiares em saúde mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "familiares_cuidadores_sm"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
