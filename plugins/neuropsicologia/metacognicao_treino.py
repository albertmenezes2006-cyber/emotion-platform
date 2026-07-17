#!/usr/bin/env python3
"""Treino metacognição"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/metacog-train", tags=["Neuropsicologia"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "metacognicao_treino", "status": "ativo",
                          "descricao": "Treino metacognição",
                          "categoria": "neuropsicologia",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "metacognicao_treino",
                          "descricao": "Treino metacognição",
                          "categoria": "neuropsicologia",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "metacognicao_treino"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
