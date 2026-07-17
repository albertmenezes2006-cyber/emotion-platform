#!/usr/bin/env python3
"""Modo manutenção"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/maintenance", tags=["maintenance_mode"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "maintenance_mode", "status": "ativo",
                          "descricao": "Modo manutenção",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "maintenance_mode"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
