#!/usr/bin/env python3
"""MBCT programa 8 semanas"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mbct", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mbct_program", "status": "ativo",
                          "descricao": "MBCT programa 8 semanas",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "mbct_program",
                          "descricao": "MBCT programa 8 semanas",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mbct_program"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
