#!/usr/bin/env python3
"""Gerador de UUIDs únicos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/uuid", tags=["uuid_generator"])

@router.get("")
async def info():
    return JSONResponse({"nome": "uuid_generator", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "uuid_generator"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
