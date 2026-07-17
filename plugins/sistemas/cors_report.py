#!/usr/bin/env python3
"""Relatório CORS"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/cors-report", tags=["cors_report"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "cors_report", "status": "ativo",
                          "descricao": "Relatório CORS",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cors_report"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
