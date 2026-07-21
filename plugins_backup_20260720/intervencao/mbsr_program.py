#!/usr/bin/env python3
"""MBSR programa completo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mbsr", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "mbsr_program", "status": "ativo",
                          "descricao": "MBSR programa completo",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "mbsr_program",
                          "descricao": "MBSR programa completo",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "mbsr_program"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
