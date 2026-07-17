#!/usr/bin/env python3
"""Definição de objetivos terapêuticos"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/objetivos-terapia", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "objetivos_terapeuticos", "status": "ativo",
                          "descricao": "Definição de objetivos terapêuticos",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "objetivos_terapeuticos",
                          "descricao": "Definição de objetivos terapêuticos",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "objetivos_terapeuticos"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
