#!/usr/bin/env python3
"""Informações do IP"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ip", tags=["ip_info"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "ip_info", "status": "ativo",
                          "descricao": "Informações do IP",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ip_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
