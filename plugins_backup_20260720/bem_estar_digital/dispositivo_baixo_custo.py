#!/usr/bin/env python3
"""Dispositivo Baixo Custo em bem estar digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/bem_estar_digit/dispositivo_baixo_custo", tags=["bem_estar_digital"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "bem_estar_digital_dispositivo_baixo_custo", "status": "ativo",
                          "descricao": "Dispositivo Baixo Custo em bem estar digital", "categoria": "bem_estar_digital",
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "bem_estar_digital_dispositivo_baixo_custo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
