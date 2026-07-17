#!/usr/bin/env python3
"""Task switching flexibilidade"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/task-switch", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "task_switching", "status": "ativo",
                          "descricao": "Task switching flexibilidade",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "task_switching",
                          "descricao": "Task switching flexibilidade",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "task_switching"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
