#!/usr/bin/env python3
"""Sequência de emails"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/email-seq", tags=["email_sequencia"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "email_sequencia", "status": "ativo",
                          "descricao": "Sequência de emails",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "email_sequencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
