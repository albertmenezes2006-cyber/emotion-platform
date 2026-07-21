#!/usr/bin/env python3
"""Plano de reintegração social"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reint-social", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "reintegracao_social_plan", "status": "ativo",
                          "descricao": "Plano de reintegração social",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "reintegracao_social_plan",
                          "descricao": "Plano de reintegração social",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "reintegracao_social_plan"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
