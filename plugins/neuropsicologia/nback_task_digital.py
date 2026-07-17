#!/usr/bin/env python3
"""N-back task digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/nback", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "nback_task_digital", "status": "ativo",
                          "descricao": "N-back task digital",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "nback_task_digital",
                          "descricao": "N-back task digital",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "nback_task_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
