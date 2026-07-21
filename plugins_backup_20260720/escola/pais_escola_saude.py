#!/usr/bin/env python3
"""Saúde mental pais e escola"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pais-escola", tags=["Escola"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "pais_escola", "status": "ativo",
                          "descricao": "Saúde mental pais e escola",
                          "versao": "1.0.0",
                          "categoria": "escola",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "pais_escola"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
