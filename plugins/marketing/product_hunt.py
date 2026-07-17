#!/usr/bin/env python3
"""Product Hunt dados"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ph", tags=["product_hunt"])

@router.get("")
async def info():
    return JSONResponse({"nome": "product_hunt", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "product_hunt"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
