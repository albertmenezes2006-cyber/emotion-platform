#!/usr/bin/env python3
"""Diagnóstico diferencial"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dif-diag", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "diferencial_diagnostico", "status": "ativo",
                          "descricao": "Diagnóstico diferencial",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "diferencial_diagnostico",
                          "descricao": "Diagnóstico diferencial",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "diferencial_diagnostico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
