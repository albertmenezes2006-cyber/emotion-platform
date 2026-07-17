#!/usr/bin/env python3
"""Programa recovery completo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/recovery-prog", tags=["Grupos"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "programa_recovery_completo", "status": "ativo",
                          "descricao": "Programa recovery completo",
                          "categoria": "grupos",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "programa_recovery_completo",
                          "descricao": "Programa recovery completo",
                          "categoria": "grupos",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "programa_recovery_completo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
