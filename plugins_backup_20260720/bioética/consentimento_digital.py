#!/usr/bin/env python3
"""Consentimento informado digital"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/consentimento-digital", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "consentimento_digital", "status": "ativo",
                          "descricao": "Consentimento informado digital",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "consentimento_digital",
                          "descricao": "Consentimento informado digital",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "consentimento_digital"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
