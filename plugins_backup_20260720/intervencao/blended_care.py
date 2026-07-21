#!/usr/bin/env python3
"""Cuidado misto presencial-digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/blended", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "blended_care", "status": "ativo",
                          "descricao": "Cuidado misto presencial-digital",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "blended_care",
                          "descricao": "Cuidado misto presencial-digital",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "blended_care"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
