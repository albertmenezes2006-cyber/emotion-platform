#!/usr/bin/env python3
"""Alzheimer e saúde familiar"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/alzheimer-familiar", tags=["Populacoes"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "alzheimer_familiar", "status": "ativo",
                          "descricao": "Alzheimer e saúde familiar",
                          "categoria": "populacoes",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "alzheimer_familiar",
                          "descricao": "Alzheimer e saúde familiar",
                          "categoria": "populacoes",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "alzheimer_familiar"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
