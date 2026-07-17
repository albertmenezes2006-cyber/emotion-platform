#!/usr/bin/env python3
"""Agendador de tarefas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cron", tags=["cron_jobs"])

@router.get("")
async def info():
    return JSONResponse({"nome": "cron_jobs", "status": "ativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cron_jobs"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
