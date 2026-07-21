#!/usr/bin/env python3
"""Tratamento transdiagnóstico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/transdiag", tags=["Intervencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "transdiagnostic_tx", "status": "ativo",
                          "descricao": "Tratamento transdiagnóstico",
                          "categoria": "intervencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "transdiagnostic_tx",
                          "descricao": "Tratamento transdiagnóstico",
                          "categoria": "intervencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "transdiagnostic_tx"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
