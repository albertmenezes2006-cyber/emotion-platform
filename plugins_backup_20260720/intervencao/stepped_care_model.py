#!/usr/bin/env python3
"""Modelo de cuidado escalonado"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/stepped-care", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "stepped_care_model", "status": "ativo",
                          "descricao": "Modelo de cuidado escalonado",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "stepped_care_model",
                          "descricao": "Modelo de cuidado escalonado",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "stepped_care_model"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
