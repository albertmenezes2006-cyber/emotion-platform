#!/usr/bin/env python3
"""Insights semanais automaticos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/insight", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "insight_semanal", "status": "ativo",
                          "descricao": "Insights semanais automaticos",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "insight_semanal"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
