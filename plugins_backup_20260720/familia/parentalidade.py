#!/usr/bin/env python3
"""Ferramentas de parentalidade positiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/parentalidade", tags=["Familia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "parentalidade", "status": "ativo",
                          "descricao": "Ferramentas de parentalidade positiva",
                          "versao": "1.0.0",
                          "categoria": "familia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "parentalidade"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
