#!/usr/bin/env python3
"""Informações sobre alienação parental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/alienacao", tags=["Familia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "alienacao_info", "status": "ativo",
                          "descricao": "Informações sobre alienação parental",
                          "versao": "1.0.0",
                          "categoria": "familia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "alienacao_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
