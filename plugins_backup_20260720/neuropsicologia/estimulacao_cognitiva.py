#!/usr/bin/env python3
"""Estimulação cognitiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/estim-cog", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "estimulacao_cognitiva", "status": "ativo",
                          "descricao": "Estimulação cognitiva",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "estimulacao_cognitiva",
                          "descricao": "Estimulação cognitiva",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "estimulacao_cognitiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
