#!/usr/bin/env python3
"""Tracker de consumo de álcool"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/alcool", tags=["Adicoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "alcohol_tracker", "status": "ativo",
                          "descricao": "Tracker de consumo de álcool",
                          "versao": "1.0.0",
                          "categoria": "adicoes",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "alcohol_tracker"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
