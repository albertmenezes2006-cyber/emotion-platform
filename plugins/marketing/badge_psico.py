#!/usr/bin/env python3
"""Badges para psicólogos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/badge", tags=["badge_psico"])

@router.get("")
async def info():
    return JSONResponse({"nome": "badge_psico", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "badge_psico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
