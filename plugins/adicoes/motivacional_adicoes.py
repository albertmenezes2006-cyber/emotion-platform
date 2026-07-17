#!/usr/bin/env python3
"""Motivação para mudança"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/motivacional-adicao", tags=["Adicoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "motivacional_adic", "status": "ativo",
                          "descricao": "Motivação para mudança",
                          "versao": "1.0.0",
                          "categoria": "adicoes",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "motivacional_adic"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
