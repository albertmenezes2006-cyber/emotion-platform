#!/usr/bin/env python3
"""Ferramentas para dissociação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dissociacao", tags=["Trauma"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dissociacao_tools", "status": "ativo",
                          "descricao": "Ferramentas para dissociação",
                          "versao": "1.0.0",
                          "categoria": "trauma",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dissociacao_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
