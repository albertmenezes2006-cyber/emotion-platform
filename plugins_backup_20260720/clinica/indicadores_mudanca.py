#!/usr/bin/env python3
"""Indicadores de mudança clínica"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/indicadores-mudanca", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "indicadores_mudanca", "status": "ativo",
                          "descricao": "Indicadores de mudança clínica",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "indicadores_mudanca",
                          "descricao": "Indicadores de mudança clínica",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "indicadores_mudanca"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
