#!/usr/bin/env python3
"""Tracker de conversão"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/conversao", tags=["conversao"])

@router.get("")
async def info():
    return JSONResponse({"nome": "conversao", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "conversao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
