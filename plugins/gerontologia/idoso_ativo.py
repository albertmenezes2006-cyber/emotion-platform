#!/usr/bin/env python3
"""Envelhecimento ativo e saudável"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/idoso-ativo", tags=["Gerontologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "idoso_ativo", "status": "ativo",
                          "descricao": "Envelhecimento ativo e saudável",
                          "versao": "1.0.0",
                          "categoria": "gerontologia",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "idoso_ativo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
