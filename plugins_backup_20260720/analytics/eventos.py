#!/usr/bin/env python3
"""Tracker de eventos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/eventos", tags=["eventos_tracker"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "eventos_tracker", "status": "ativo",
                          "descricao": "Tracker de eventos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "eventos_tracker"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
