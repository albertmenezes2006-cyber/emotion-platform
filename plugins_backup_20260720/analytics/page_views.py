#!/usr/bin/env python3
"""Contador de visualizações"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pageviews", tags=["page_views"])

@router.get("")
async def info():
    return JSONResponse({"nome": "page_views", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "page_views"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
