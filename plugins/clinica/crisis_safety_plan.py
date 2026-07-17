#!/usr/bin/env python3
"""Plano de segurança em crise"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/crisis-plan", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "crisis_safety_plan", "status": "ativo",
                          "descricao": "Plano de segurança em crise",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "crisis_safety_plan",
                          "descricao": "Plano de segurança em crise",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "crisis_safety_plan"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
