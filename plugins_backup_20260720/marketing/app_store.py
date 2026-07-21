#!/usr/bin/env python3
"""Preparação App Store"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/app-store", tags=["app_store_prep"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "app_store_prep", "status": "ativo",
                          "descricao": "Preparação App Store",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "app_store_prep"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
