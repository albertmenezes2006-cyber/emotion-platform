#!/usr/bin/env python3
"""Peer Support Veterans"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/peer_support_veterans", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_peer_support_veterans","s":"ativo","d":"Peer Support Veterans","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_peer_support_veterans"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
