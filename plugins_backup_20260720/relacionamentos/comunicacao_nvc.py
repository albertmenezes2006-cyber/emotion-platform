#!/usr/bin/env python3
"""Comunicação Não-Violenta"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/nvc", tags=["Relacionamentos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "nvc_tools", "status": "ativo",
                          "descricao": "Comunicação Não-Violenta",
                          "versao": "1.0.0",
                          "categoria": "relacionamentos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "nvc_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
