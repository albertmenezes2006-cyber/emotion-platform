#!/usr/bin/env python3
"""Saúde mental no home office"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/home-office", tags=["Corporativo"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "home_office_saude", "status": "ativo",
                          "descricao": "Saúde mental no home office",
                          "versao": "1.0.0",
                          "categoria": "corporativo",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "home_office_saude"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
