#!/usr/bin/env python3
"""Psicologia e meios de comunicação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/midia-psi", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "medios_comunicacao_psi", "status": "ativo",
                          "descricao": "Psicologia e meios de comunicação",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "medios_comunicacao_psi",
                          "descricao": "Psicologia e meios de comunicação",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "medios_comunicacao_psi"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
