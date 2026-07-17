#!/usr/bin/env python3
"""Metricas basicas do sistema"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime
import os, sys

router = APIRouter(prefix="/api/v1/metricas", tags=["Métricas"])
_inicio = datetime.utcnow()
_requests = 0

@router.get("")
async def metricas():
    global _requests
    _requests += 1
    uptime = (datetime.utcnow() - _inicio).total_seconds()
    return JSONResponse({
        "uptime_segundos": round(uptime),
        "uptime_horas": round(uptime/3600, 2),
        "requests_totais": _requests,
        "python_versao": sys.version.split()[0],
        "ambiente": os.getenv("RENDER", "local"),
        "timestamp": datetime.utcnow().isoformat()
    })

class MetricasPlugin(PluginBase):
    name = "metricas_sistema"
    def setup(self, app): app.include_router(router)
plugin = MetricasPlugin()
