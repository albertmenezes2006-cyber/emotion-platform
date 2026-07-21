#!/usr/bin/env python3
"""Suporte na transição de carreira"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/transicao-carreira", tags=["Carreira"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "transicao_carreira", "status": "ativo",
                          "descricao": "Suporte na transição de carreira",
                          "versao": "1.0.0",
                          "categoria": "carreira",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "transicao_carreira"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
