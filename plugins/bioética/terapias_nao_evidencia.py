#!/usr/bin/env python3
"""Terapias sem evidência científica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/sem-evidencia", tags=["Bioetica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "terapias_nao_evidencia", "status": "ativo",
                          "descricao": "Terapias sem evidência científica",
                          "categoria": "bioetica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "terapias_nao_evidencia",
                          "descricao": "Terapias sem evidência científica",
                          "categoria": "bioetica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "terapias_nao_evidencia"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
