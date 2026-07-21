#!/usr/bin/env python3
"""Monitoramento progresso terapêutico"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/progresso-terapia", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "progresso_terapeutico", "status": "ativo",
                          "descricao": "Monitoramento progresso terapêutico",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "progresso_terapeutico",
                          "descricao": "Monitoramento progresso terapêutico",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "progresso_terapeutico"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
