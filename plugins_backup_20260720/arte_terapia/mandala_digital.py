#!/usr/bin/env python3
"""Mandala digital para meditação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mandala", tags=["Arte Terapia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mandala_digital", "status": "ativo",
                          "descricao": "Mandala digital para meditação",
                          "versao": "1.0.0",
                          "categoria": "arte_terapia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mandala_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
