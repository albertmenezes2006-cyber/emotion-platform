#!/usr/bin/env python3
"""Gerenciador de sessões"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sessions", tags=["session_manager"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "session_manager", "status": "ativo",
                          "descricao": "Gerenciador de sessões",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "session_manager"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
