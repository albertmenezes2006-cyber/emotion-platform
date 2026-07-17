#!/usr/bin/env python3
"""Peer Support Paid em saude coletiva mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_coletiva_/peer_support_paid", tags=["saude_coletiva_mental"])
@router.get("")
async def info():
    return JSONResponse({"plugin":"saude_coletiva_menta_peer_support_paid","status":"ativo","desc":"Peer Support Paid em saude coletiva mental","ts":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_coletiva_menta_peer_support_paid"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
