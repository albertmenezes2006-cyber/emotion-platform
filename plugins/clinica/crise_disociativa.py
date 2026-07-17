#!/usr/bin/env python3
"""Crise dissociativa manejo"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/crise-dissoc", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "crise_disociativa", "status": "ativo",
                          "descricao": "Crise dissociativa manejo",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "crise_disociativa",
                          "descricao": "Crise dissociativa manejo",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "crise_disociativa"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
