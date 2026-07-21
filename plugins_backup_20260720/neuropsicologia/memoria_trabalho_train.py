#!/usr/bin/env python3
"""Treino memória de trabalho"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/mwm-train", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "memoria_trabalho_train", "status": "ativo",
                          "descricao": "Treino memória de trabalho",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "memoria_trabalho_train",
                          "descricao": "Treino memória de trabalho",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "memoria_trabalho_train"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
