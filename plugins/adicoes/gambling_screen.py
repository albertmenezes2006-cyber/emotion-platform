#!/usr/bin/env python3
"""Triagem de jogo problemático"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/jogo", tags=["Adicoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "gambling_screen", "status": "ativo",
                          "descricao": "Triagem de jogo problemático",
                          "versao": "1.0.0",
                          "categoria": "adicoes",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "gambling_screen"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
