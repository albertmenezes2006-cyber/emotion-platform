#!/usr/bin/env python3
"""Série temporal de humor"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/time-series", tags=["Machine Learning"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "time_series_mood", "status": "ativo",
                          "descricao": "Série temporal de humor",
                          "versao": "1.0.0",
                          "categoria": "machine_learning",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "time_series_mood"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
