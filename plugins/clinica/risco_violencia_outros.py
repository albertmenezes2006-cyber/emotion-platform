#!/usr/bin/env python3
"""Risco de violência a terceiros"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/risco-violencia", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "risco_violencia_outros", "status": "ativo",
                          "descricao": "Risco de violência a terceiros",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "risco_violencia_outros",
                          "descricao": "Risco de violência a terceiros",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "risco_violencia_outros"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
