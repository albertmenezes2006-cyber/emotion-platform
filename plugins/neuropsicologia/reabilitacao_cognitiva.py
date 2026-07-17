#!/usr/bin/env python3
"""Reabilitação cognitiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/reab-cog", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "reabilitacao_cognitiva", "status": "ativo",
                          "descricao": "Reabilitação cognitiva",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "reabilitacao_cognitiva",
                          "descricao": "Reabilitação cognitiva",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "reabilitacao_cognitiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
