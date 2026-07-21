#!/usr/bin/env python3
"""Keepalive endpoint para nao dormir no Render"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/keepalive", tags=["Sistema"])

@router.get("")
async def keepalive():
    return JSONResponse({"alive": True, "ts": datetime.utcnow().isoformat(),
                         "msg": "Emotion Platform ativo"})

class KeepalivePlugin(PluginBase):
    name = "ping_keepalive"
    def setup(self, app): app.include_router(router)
plugin = KeepalivePlugin()
