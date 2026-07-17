#!/usr/bin/env python3
"""Plano pós-alta hospitalar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/pos-alta", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "pós_alta_plano", "status": "ativo",
                          "descricao": "Plano pós-alta hospitalar",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "pós_alta_plano",
                          "descricao": "Plano pós-alta hospitalar",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "pós_alta_plano"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
