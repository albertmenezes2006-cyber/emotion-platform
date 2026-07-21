#!/usr/bin/env python3
"""Informações do deploy"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/deploy", tags=["deploy_info"])

@router.get("")
async def info():
    return JSONResponse({"nome": "deploy_info", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "deploy_info"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
