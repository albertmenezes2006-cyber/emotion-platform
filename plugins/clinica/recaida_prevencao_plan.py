#!/usr/bin/env python3
"""Plano de prevenção de recaída"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/recaida-plan", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "recaida_prevencao_plan", "status": "ativo",
                          "descricao": "Plano de prevenção de recaída",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "recaida_prevencao_plan",
                          "descricao": "Plano de prevenção de recaída",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "recaida_prevencao_plan"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
