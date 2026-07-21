#!/usr/bin/env python3
"""Beneficência na psicologia"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/beneficencia", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "beneficencia_psicologia", "status": "ativo",
                          "descricao": "Beneficência na psicologia",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "beneficencia_psicologia",
                          "descricao": "Beneficência na psicologia",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "beneficencia_psicologia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
