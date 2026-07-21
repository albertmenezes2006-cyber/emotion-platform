#!/usr/bin/env python3
"""Letramento digital em saúde"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/letramento-digital", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "digital_mental_health_lit", "status": "ativo",
                          "descricao": "Letramento digital em saúde",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "digital_mental_health_lit",
                          "descricao": "Letramento digital em saúde",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "digital_mental_health_lit"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
