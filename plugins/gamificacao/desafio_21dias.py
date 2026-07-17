#!/usr/bin/env python3
"""Desafio de 21 dias"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/desafio-21", tags=["Gamificacao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "desafio_21", "status": "ativo",
                          "descricao": "Desafio de 21 dias",
                          "versao": "1.0.0",
                          "categoria": "gamificacao",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "desafio_21"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
