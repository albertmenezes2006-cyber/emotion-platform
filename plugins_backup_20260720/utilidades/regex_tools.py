#!/usr/bin/env python3
"""Ferramentas de regex"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/regex", tags=["regex_tools"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "regex_tools", "status": "ativo",
                          "descricao": "Ferramentas de regex",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "regex_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
