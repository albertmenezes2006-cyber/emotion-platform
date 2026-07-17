#!/usr/bin/env python3
"""Remediação cognitiva psicose"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/remediacao-cog", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "remediacão_cognitiva", "status": "ativo",
                          "descricao": "Remediação cognitiva psicose",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "remediacão_cognitiva",
                          "descricao": "Remediação cognitiva psicose",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "remediacão_cognitiva"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
