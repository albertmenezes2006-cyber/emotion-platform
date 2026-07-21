#!/usr/bin/env python3
"""Clarificação de valores profissionais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/valores-carreira", tags=["Carreira"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "valores_carreira", "status": "ativo",
                          "descricao": "Clarificação de valores profissionais",
                          "versao": "1.0.0",
                          "categoria": "carreira",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "valores_carreira"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
