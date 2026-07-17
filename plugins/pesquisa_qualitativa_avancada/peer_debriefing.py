#!/usr/bin/env python3
"""Peer Debriefing"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/pesquisa_qua/peer_debriefing", tags=["pesquisa_qualitativa_avancada"])
@router.get("")
async def info():
    return JSONResponse({"p":"pesquisa_qualitati_peer_debriefing","s":"ativo","d":"Peer Debriefing","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "pesquisa_qualitati_peer_debriefing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
