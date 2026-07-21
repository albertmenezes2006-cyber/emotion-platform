#!/usr/bin/env python3
"""Flanker task atenção"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/flanker", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "flanker_task", "status": "ativo",
                          "descricao": "Flanker task atenção",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "flanker_task",
                          "descricao": "Flanker task atenção",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "flanker_task"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
