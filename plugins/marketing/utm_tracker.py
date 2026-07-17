#!/usr/bin/env python3
"""Tracker de UTM params"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/utm", tags=["utm_tracker"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "utm_tracker", "status": "ativo",
                          "descricao": "Tracker de UTM params",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "utm_tracker"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
