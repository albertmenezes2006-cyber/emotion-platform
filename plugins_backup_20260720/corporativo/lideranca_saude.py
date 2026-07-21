#!/usr/bin/env python3
"""Liderança e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/lideranca-saude", tags=["Corporativo"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "lideranca_saude", "status": "ativo",
                          "descricao": "Liderança e saúde mental",
                          "versao": "1.0.0",
                          "categoria": "corporativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "lideranca_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
