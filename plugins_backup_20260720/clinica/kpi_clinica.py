#!/usr/bin/env python3
"""KPIs da clinica em tempo real"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/kpi-clinica", tags=["Essencial"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "kpi_clinica_dashboard", "status": "ativo",
                          "descricao": "KPIs da clinica em tempo real",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "kpi_clinica_dashboard"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
