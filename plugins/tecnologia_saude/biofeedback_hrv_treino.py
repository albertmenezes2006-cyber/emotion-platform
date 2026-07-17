#!/usr/bin/env python3
"""Treino de HRV biofeedback"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/hrv-treino", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "biofeedback_hrv_treino", "status": "ativo",
                          "descricao": "Treino de HRV biofeedback",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "biofeedback_hrv_treino",
                          "descricao": "Treino de HRV biofeedback",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "biofeedback_hrv_treino"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
