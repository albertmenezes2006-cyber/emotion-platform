#!/usr/bin/env python3
"""Avaliação automutilação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/automutilacao", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "risco_automutilacao", "status": "ativo",
                          "descricao": "Avaliação automutilação",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "risco_automutilacao",
                          "descricao": "Avaliação automutilação",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "risco_automutilacao"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
