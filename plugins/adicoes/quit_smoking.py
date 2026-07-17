#!/usr/bin/env python3
"""Programa para parar de fumar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/parar-fumar", tags=["Adicoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "quit_smoking", "status": "ativo",
                          "descricao": "Programa para parar de fumar",
                          "versao": "1.0.0",
                          "categoria": "adicoes",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "quit_smoking"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
