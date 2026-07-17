#!/usr/bin/env python3
"""Cuidado em demências"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/demencia", tags=["Gerontologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "demencia_cuidado", "status": "ativo",
                          "descricao": "Cuidado em demências",
                          "versao": "1.0.0",
                          "categoria": "gerontologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "demencia_cuidado"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
