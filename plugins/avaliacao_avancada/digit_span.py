#!/usr/bin/env python3
"""Digit Span memória de trabalho"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/digit-span", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "digit_span", "status": "ativo",
                          "descricao": "Digit Span memória de trabalho",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "digit_span",
                          "descricao": "Digit Span memória de trabalho",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "digit_span"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
