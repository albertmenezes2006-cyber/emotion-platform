#!/usr/bin/env python3
"""Peer Coaching"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/psicologia_o/peer_coaching", tags=["psicologia_organizacional_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"psicologia_organiz_peer_coaching","s":"ativo","d":"Peer Coaching","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "psicologia_organiz_peer_coaching"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
