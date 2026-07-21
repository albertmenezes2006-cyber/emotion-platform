#!/usr/bin/env python3
"""Shinrin-yoku banho de floresta"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/shinrin", tags=["Natureza"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "shinrin_yoku", "status": "ativo",
                          "descricao": "Shinrin-yoku banho de floresta",
                          "versao": "1.0.0",
                          "categoria": "natureza",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "shinrin_yoku"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
