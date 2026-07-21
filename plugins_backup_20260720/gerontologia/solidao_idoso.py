#!/usr/bin/env python3
"""Solidão e isolamento no idoso"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/solidao", tags=["Gerontologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "solidao_idoso", "status": "ativo",
                          "descricao": "Solidão e isolamento no idoso",
                          "versao": "1.0.0",
                          "categoria": "gerontologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "solidao_idoso"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
