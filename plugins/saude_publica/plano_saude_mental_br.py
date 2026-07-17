#!/usr/bin/env python3
"""Plano de Saúde Mental Brasil"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/plano-sm-br", tags=["Saude Publica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "plano_saude_mental_br", "status": "ativo",
                          "descricao": "Plano de Saúde Mental Brasil",
                          "categoria": "saude_publica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "plano_saude_mental_br",
                          "descricao": "Plano de Saúde Mental Brasil",
                          "categoria": "saude_publica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "plano_saude_mental_br"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
