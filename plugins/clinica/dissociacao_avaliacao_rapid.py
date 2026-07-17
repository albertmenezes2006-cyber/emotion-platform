#!/usr/bin/env python3
"""Avaliação rápida dissociação"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/dissoc-rapid", tags=["Clinica"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "dissociacao_avaliacao_rapid", "status": "ativo",
                          "descricao": "Avaliação rápida dissociação",
                          "categoria": "clinica",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "dissociacao_avaliacao_rapid",
                          "descricao": "Avaliação rápida dissociação",
                          "categoria": "clinica",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "dissociacao_avaliacao_rapid"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
