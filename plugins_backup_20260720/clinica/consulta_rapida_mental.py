#!/usr/bin/env python3
"""Consulta rápida saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/consulta-rapida", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "consulta_rapida_mental", "status": "ativo",
                          "descricao": "Consulta rápida saúde mental",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "consulta_rapida_mental",
                          "descricao": "Consulta rápida saúde mental",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "consulta_rapida_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
