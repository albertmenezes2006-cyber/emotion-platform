#!/usr/bin/env python3
"""Reuniões saudáveis e bem-estar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reunioes", tags=["Corporativo"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "reunioes_saudaveis", "status": "ativo",
                          "descricao": "Reuniões saudáveis e bem-estar",
                          "versao": "1.0.0",
                          "categoria": "corporativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "reunioes_saudaveis"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
