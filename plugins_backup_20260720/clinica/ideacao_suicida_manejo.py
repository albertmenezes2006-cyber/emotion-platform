#!/usr/bin/env python3
"""Ideação suicida manejo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/ideacao-manejo", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "ideacao_suicida_manejo", "status": "ativo",
                          "descricao": "Ideação suicida manejo",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "ideacao_suicida_manejo",
                          "descricao": "Ideação suicida manejo",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "ideacao_suicida_manejo"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
