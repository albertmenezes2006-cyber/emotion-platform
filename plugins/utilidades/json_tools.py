#!/usr/bin/env python3
"""Ferramentas JSON"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/json", tags=["json_tools"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "json_tools", "status": "ativo",
                          "descricao": "Ferramentas JSON",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "json_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
