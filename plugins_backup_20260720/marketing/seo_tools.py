#!/usr/bin/env python3
"""Ferramentas de SEO"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/seo", tags=["seo_tools"])

@router.get("")
async def info():
    return JSONResponse({"nome": "seo_tools", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "seo_tools"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
