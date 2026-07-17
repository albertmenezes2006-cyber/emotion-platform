#!/usr/bin/env python3
"""Cuidado baseado em mensuração"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mbc", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "measurement_based_care", "status": "ativo",
                          "descricao": "Cuidado baseado em mensuração",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "measurement_based_care",
                          "descricao": "Cuidado baseado em mensuração",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "measurement_based_care"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
