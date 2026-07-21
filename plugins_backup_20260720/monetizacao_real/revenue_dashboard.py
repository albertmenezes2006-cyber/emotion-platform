#!/usr/bin/env python3
"""Dashboard de receita em tempo real"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/revenue", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "revenue_dash", "status": "ativo",
                          "descricao": "Dashboard de receita em tempo real",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "revenue_dash"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
