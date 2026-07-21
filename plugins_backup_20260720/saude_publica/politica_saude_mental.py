#!/usr/bin/env python3
"""Política Nacional de Saúde Mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/politica-sm", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "politica_saude_mental", "status": "ativo",
                          "descricao": "Política Nacional de Saúde Mental",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "politica_saude_mental",
                          "descricao": "Política Nacional de Saúde Mental",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "politica_saude_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
