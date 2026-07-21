#!/usr/bin/env python3
"""Informações de CORS"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cors", tags=["cors_info"])

@router.get("")
async def info():
    return JSONResponse({"nome": "cors_info", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cors_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
