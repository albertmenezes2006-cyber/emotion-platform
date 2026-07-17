#!/usr/bin/env python3
"""Competência cultural"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/competencia-cultural", tags=["Prevencao"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "cultural_competence", "status": "ativo",
                          "descricao": "Competência cultural",
                          "categoria": "prevencao",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "cultural_competence",
                          "descricao": "Competência cultural",
                          "categoria": "prevencao",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "cultural_competence"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
