#!/usr/bin/env python3
"""Saúde mental na escola"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/escola", tags=["Escola"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "saude_escolar", "status": "ativo",
                          "descricao": "Saúde mental na escola",
                          "versao": "1.0.0",
                          "categoria": "escola",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "saude_escolar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
