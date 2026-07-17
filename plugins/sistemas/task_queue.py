#!/usr/bin/env python3
"""Fila de tarefas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/tasks", tags=["task_queue"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "task_queue", "status": "ativo",
                          "descricao": "Fila de tarefas",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "task_queue"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
