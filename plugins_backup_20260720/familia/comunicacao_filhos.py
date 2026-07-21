#!/usr/bin/env python3
"""Comunicação com filhos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/filhos", tags=["Familia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "comunicacao_filhos", "status": "ativo",
                          "descricao": "Comunicação com filhos",
                          "versao": "1.0.0",
                          "categoria": "familia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "comunicacao_filhos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
