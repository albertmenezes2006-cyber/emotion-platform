#!/usr/bin/env python3
"""Calendário de conteúdo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/content-cal", tags=["Marketing"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "content_calendar", "status": "ativo",
                          "descricao": "Calendário de conteúdo",
                          "versao": "1.0.0",
                          "categoria": "marketing",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "content_calendar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
