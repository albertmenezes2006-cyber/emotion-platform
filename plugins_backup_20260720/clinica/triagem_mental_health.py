#!/usr/bin/env python3
"""Triagem em saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/triagem-mental", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "triagem_mental_health", "status": "ativo",
                          "descricao": "Triagem em saúde mental",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "triagem_mental_health",
                          "descricao": "Triagem em saúde mental",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "triagem_mental_health"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
