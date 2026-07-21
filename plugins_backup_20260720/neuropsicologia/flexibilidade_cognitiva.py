#!/usr/bin/env python3
"""Flexibilidade cognitiva treino"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/flex-cog", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "flexibilidade_cognitiva", "status": "ativo",
                          "descricao": "Flexibilidade cognitiva treino",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "flexibilidade_cognitiva",
                          "descricao": "Flexibilidade cognitiva treino",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "flexibilidade_cognitiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
