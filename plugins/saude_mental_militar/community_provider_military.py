#!/usr/bin/env python3
"""Community Provider Military"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
router = APIRouter(prefix="/api/v1/saude_mental/community_provider_military", tags=["saude_mental_militar"])
@router.get("")
async def info():
    return JSONResponse({"p":"saude_mental_milit_community_provider_milita","s":"ativo","d":"Community Provider Military","t":datetime.utcnow().isoformat()})
class Plugin(PluginBase):
    name = "saude_mental_milit_community_provider_milita"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
