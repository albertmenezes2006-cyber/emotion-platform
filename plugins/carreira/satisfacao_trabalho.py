#!/usr/bin/env python3
"""Avaliação de satisfação no trabalho"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sat-trabalho", tags=["Carreira"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "satisfacao_trab", "status": "ativo",
                          "descricao": "Avaliação de satisfação no trabalho",
                          "versao": "1.0.0",
                          "categoria": "carreira",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "satisfacao_trab"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
