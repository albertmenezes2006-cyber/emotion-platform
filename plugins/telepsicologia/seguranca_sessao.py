#!/usr/bin/env python3
"""Segurança na sessão online"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/seg-sessao", tags=["Telepsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "seguranca_sessao", "status": "ativo",
                          "descricao": "Segurança na sessão online",
                          "versao": "1.0.0",
                          "categoria": "telepsicologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "seguranca_sessao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
