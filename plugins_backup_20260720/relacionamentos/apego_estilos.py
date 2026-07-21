#!/usr/bin/env python3
"""Estilos de apego adulto"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/apego", tags=["Relacionamentos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "attachment_styles", "status": "ativo",
                          "descricao": "Estilos de apego adulto",
                          "versao": "1.0.0",
                          "categoria": "relacionamentos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "attachment_styles"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
