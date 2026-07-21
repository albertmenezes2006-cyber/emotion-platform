#!/usr/bin/env python3
"""Suporte digital ao luto"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/luto", tags=["Luto"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "luto_guiado", "status": "ativo",
                          "descricao": "Suporte digital ao luto",
                          "versao": "1.0.0",
                          "categoria": "luto",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "luto_guiado"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
