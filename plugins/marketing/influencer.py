#!/usr/bin/env python3
"""Kit para influencers"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/influencer", tags=["influencer_kit"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "influencer_kit", "status": "ativo",
                          "descricao": "Kit para influencers",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "influencer_kit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
