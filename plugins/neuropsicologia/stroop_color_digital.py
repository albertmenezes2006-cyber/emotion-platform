#!/usr/bin/env python3
"""Stroop digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/stroop-digital", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "stroop_color_digital", "status": "ativo",
                          "descricao": "Stroop digital",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "stroop_color_digital",
                          "descricao": "Stroop digital",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "stroop_color_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
