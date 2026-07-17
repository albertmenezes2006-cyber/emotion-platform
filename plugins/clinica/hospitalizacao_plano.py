#!/usr/bin/env python3
"""Plano de hospitalização"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/hospital-plan", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "hospitalizacao_plano", "status": "ativo",
                          "descricao": "Plano de hospitalização",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "hospitalizacao_plano",
                          "descricao": "Plano de hospitalização",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "hospitalizacao_plano"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
