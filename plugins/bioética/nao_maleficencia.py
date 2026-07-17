#!/usr/bin/env python3
"""Não-maleficência"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/nao-malef", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "nao_maleficencia", "status": "ativo",
                          "descricao": "Não-maleficência",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "nao_maleficencia",
                          "descricao": "Não-maleficência",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "nao_maleficencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
