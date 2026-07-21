#!/usr/bin/env python3
"""Stop signal task"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/stop-signal", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "stop_signal_digital", "status": "ativo",
                          "descricao": "Stop signal task",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "stop_signal_digital",
                          "descricao": "Stop signal task",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "stop_signal_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
