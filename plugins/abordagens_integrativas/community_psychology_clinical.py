#!/usr/bin/env python3
"""Community Psychology Clinical"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/abordagens_i/community_psychology_clinica", tags=["abordagens_integrativas"])
@router.get("")
async def info():
    return JSONResponse({"p":"abordagens_integra_community_psychology_clin","s":"ativo","d":"Community Psychology Clinical","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "abordagens_integra_community_psychology_clin"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
