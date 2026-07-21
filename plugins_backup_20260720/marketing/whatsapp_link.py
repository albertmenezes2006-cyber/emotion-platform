#!/usr/bin/env python3
"""Gerador de links WhatsApp"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/whatsapp", tags=["whatsapp_link"])

@router.get("")
async def info():
    return JSONResponse({"nome": "whatsapp_link", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "whatsapp_link"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
