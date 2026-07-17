#!/usr/bin/env python3
"""Jejum intermitente e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/jejum", tags=["Nutricao Mental"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "jejum_mental", "status": "ativo",
                          "descricao": "Jejum intermitente e saúde mental",
                          "versao": "1.0.0",
                          "categoria": "nutricao_mental",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "jejum_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
