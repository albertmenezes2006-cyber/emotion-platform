#!/usr/bin/env python3
"""Exposição prolongada Foa"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pe-protocol", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "prolonged_exposure", "status": "ativo",
                          "descricao": "Exposição prolongada Foa",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "prolonged_exposure",
                          "descricao": "Exposição prolongada Foa",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "prolonged_exposure"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
