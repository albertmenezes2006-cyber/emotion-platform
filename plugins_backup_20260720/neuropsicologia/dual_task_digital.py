#!/usr/bin/env python3
"""Dual task cognitivo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dual-task", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dual_task_digital", "status": "ativo",
                          "descricao": "Dual task cognitivo",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dual_task_digital",
                          "descricao": "Dual task cognitivo",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dual_task_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
