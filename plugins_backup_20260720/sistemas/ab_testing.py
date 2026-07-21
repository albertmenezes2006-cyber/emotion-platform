#!/usr/bin/env python3
"""Testes A/B simples"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ab", tags=["ab_testing"])

@router.get("")
async def info():
    return JSONResponse({"nome": "ab_testing", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ab_testing"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
