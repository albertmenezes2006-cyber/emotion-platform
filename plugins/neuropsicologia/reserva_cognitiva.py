#!/usr/bin/env python3
"""Reserva cognitiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reserva-cog", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "reserva_cognitiva", "status": "ativo",
                          "descricao": "Reserva cognitiva",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "reserva_cognitiva",
                          "descricao": "Reserva cognitiva",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "reserva_cognitiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
