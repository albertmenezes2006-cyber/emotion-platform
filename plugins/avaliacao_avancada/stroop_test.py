#!/usr/bin/env python3
"""Stroop Test atenção seletiva"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/stroop", tags=["Avaliacao Avancada"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "stroop_test", "status": "ativo",
                          "descricao": "Stroop Test atenção seletiva",
                          "categoria": "avaliacao_avancada",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "stroop_test",
                          "descricao": "Stroop Test atenção seletiva",
                          "categoria": "avaliacao_avancada",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "stroop_test"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
