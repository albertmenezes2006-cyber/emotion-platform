#!/usr/bin/env python3
"""Análise de retenção"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/retencao", tags=["retencao"])

@router.get("")
async def endpoint():
    return JSONResponse({"nome": "retencao", "status": "ativo",
                          "descricao": "Análise de retenção",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "retencao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
