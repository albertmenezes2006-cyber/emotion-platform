#!/usr/bin/env python3
"""Profiling de performance"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/profile", tags=["profiling"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "profiling", "status": "ativo",
                          "descricao": "Profiling de performance",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "profiling"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
