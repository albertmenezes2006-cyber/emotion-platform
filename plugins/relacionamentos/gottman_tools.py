#!/usr/bin/env python3
"""Ferramentas Gottman para casais"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/gottman", tags=["Relacionamentos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "gottman_tools", "status": "ativo",
                          "descricao": "Ferramentas Gottman para casais",
                          "versao": "1.0.0",
                          "categoria": "relacionamentos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "gottman_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
