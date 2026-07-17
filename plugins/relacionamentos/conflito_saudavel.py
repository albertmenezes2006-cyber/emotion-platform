#!/usr/bin/env python3
"""Resolução saudável de conflitos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/conflito", tags=["Relacionamentos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "conflito_saudavel", "status": "ativo",
                          "descricao": "Resolução saudável de conflitos",
                          "versao": "1.0.0",
                          "categoria": "relacionamentos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "conflito_saudavel"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
