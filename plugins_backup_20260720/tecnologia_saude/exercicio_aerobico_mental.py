#!/usr/bin/env python3
"""Exercício aeróbico e saúde mental"""
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from plugins.plugin_base import PluginBase
from datetime import datetime

router = APIRouter(prefix="/api/v1/aerobico-mental", tags=["Tecnologia Saude"])

@router.get("")
async def info():
    return JSONResponse({"plugin": "exercicio_aerobico_mental", "status": "ativo",
                          "descricao": "Exercício aeróbico e saúde mental",
                          "categoria": "tecnologia_saude",
                          "versao": "1.0.0",
                          "timestamp": datetime.utcnow().isoformat()})

@router.get("/info")
async def info_detalhada():
    return JSONResponse({"nome": "exercicio_aerobico_mental",
                          "descricao": "Exercício aeróbico e saúde mental",
                          "categoria": "tecnologia_saude",
                          "recursos": [],
                          "referencias": [],
                          "timestamp": datetime.utcnow().isoformat()})

class Plugin(PluginBase):
    name = "exercicio_aerobico_mental"
    def setup(self, app): app.include_router(router)
plugin = Plugin()
