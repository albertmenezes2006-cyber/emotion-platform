#!/usr/bin/env python3
"""Hexaco Modelo em bem estar digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem_estar_digit/hexaco_modelo", tags=["bem_estar_digital"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_digital_hexaco_modelo", "status": "ativo",
                          "descricao": "Hexaco Modelo em bem estar digital", "categoria": "bem_estar_digital",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_digital_hexaco_modelo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
