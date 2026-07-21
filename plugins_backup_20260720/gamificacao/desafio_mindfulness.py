#!/usr/bin/env python3
"""Desafio de mindfulness"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/desafio-mindful", tags=["Gamificacao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "desafio_mindful", "status": "ativo",
                          "descricao": "Desafio de mindfulness",
                          "versao": "1.0.0",
                          "categoria": "gamificacao",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "desafio_mindful"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
