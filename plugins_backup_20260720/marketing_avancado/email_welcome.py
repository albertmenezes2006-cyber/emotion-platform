#!/usr/bin/env python3
"""Sequencia de boas-vindas email"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/email-welcome", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "email_welcome_seq", "status": "ativo",
                          "descricao": "Sequencia de boas-vindas email",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "email_welcome_seq"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
