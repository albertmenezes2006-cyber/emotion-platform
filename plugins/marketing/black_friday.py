#!/usr/bin/env python3
"""Página Black Friday"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/black-friday", tags=["black_friday"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "black_friday", "status": "ativo",
                          "descricao": "Página Black Friday",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "black_friday"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
